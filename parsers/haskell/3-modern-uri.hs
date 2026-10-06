{-# LANGUAGE OverloadedStrings #-}

-- Signal: modern-uri, 40 reverse deps. Megaparsec-based URI parser with
-- refined phantom-typed RText labels and smart constructors.
--
-- The library stores userinfo as (uiUsername, uiPassword) separately — no
-- combined userinfo string, so userinfo is EXCLUDE.
-- The library stores query as [QueryParam] — no raw string, so query is EXCLUDE.
-- Path is stored as (trailingSlash :: Bool, [RText 'PathPiece]); segments are
-- joined here only to produce a comparable string — no further interpretation.
-- authority is EXCLUDE — not provided as a string, only as typed components.

import Text.URI ( URI, mkURI, unRText
                , uriScheme, uriAuthority, uriPath, uriQuery, uriFragment
                , Authority(..), UserInfo(..), QueryParam(..) )
import Control.Exception (try, evaluate, SomeException)
import Data.Aeson (encode, object, (.=))
import qualified Data.Aeson.Key as AK
import qualified Data.ByteString.Lazy.Char8 as BL
import qualified Data.Text as T
import System.Environment (getArgs)
import System.Exit (exitFailure)

toMaybe :: String -> Maybe String
toMaybe "" = Nothing
toMaybe s  = Just s

qpPair :: QueryParam -> (AK.Key, String)
qpPair (QueryFlag k)    = (AK.fromString (T.unpack (unRText k)), "")
qpPair (QueryParam k v) = (AK.fromString (T.unpack (unRText k)), T.unpack (unRText v))

main :: IO ()
main = do
    args <- getArgs
    case args of
        (url:_) -> do
            result <- try (evaluate =<< mkURI (T.pack url)) :: IO (Either SomeException URI)
            BL.putStrLn $ encode $ case result of
                Left err -> object
                    [ "error"   .= show err
                    , "raw_url" .= url
                    ]
                Right u  ->
                    let mAuth  = case uriAuthority u of { Right a -> Just a; _ -> Nothing }
                        ui     = mAuth >>= authUserInfo
                        uname  = fmap (toMaybe . T.unpack . unRText . uiUsername) ui >>= id
                        passwd = fmap (toMaybe . T.unpack . unRText) (ui >>= uiPassword) >>= id
                        host   = fmap (toMaybe . T.unpack . unRText . authHost) mAuth >>= id
                        port   = fmap show (mAuth >>= authPort)                        
                        frag   = fmap (toMaybe . T.unpack . unRText) (uriFragment u) >>= id
                    in object
                        [ "scheme"     .= fmap (T.unpack . unRText) (uriScheme u)
                        , "authority"  .= ("EXCLUDE" :: String)
                        , "userinfo"   .= ("EXCLUDE" :: String)
                        , "username"   .= uname
                        , "password"   .= passwd
                        , "host"       .= host
                        , "port"       .= port
                        , "path"       .= ("EXCLUDE" :: String)
                        , "query"      .= ("EXCLUDE" :: String)
                        , "query_dict" .= ("EXCLUDE" :: String)
                        , "fragment"   .= frag
                        , "raw_url"    .= url
                        ]
        [] ->
            BL.putStrLn (encode (object ["error" .= ("No URL provided" :: String)]))
            >> exitFailure