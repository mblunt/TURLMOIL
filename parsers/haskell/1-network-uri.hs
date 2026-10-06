{-# LANGUAGE OverloadedStrings #-}


-- Signal: network-uri, 414 reverse deps. RFC 3986 foundational parser split
-- from the network package at network-2.6; the base URI type used by most of
-- the Haskell HTTP ecosystem (http-client, warp, servant all depend on it).
--
-- Raw values are returned as-is: uriScheme includes ':', uriQuery includes '?',
-- uriFragment includes '#', uriPort includes ':', uriUserInfo includes '@'.
-- authority/username/password are EXCLUDE — not directly provided as strings.

import Network.URI (parseURI, URI(..), URIAuth(..))
import Data.Aeson (encode, object, (.=))
import qualified Data.ByteString.Lazy.Char8 as BL
import System.Environment (getArgs)
import System.Exit (exitFailure)

toMaybe :: String -> Maybe String
toMaybe "" = Nothing
toMaybe s  = Just s

main :: IO ()
main = do
    args <- getArgs
    case args of
        (url:_) ->
            BL.putStrLn $ encode $ case parseURI url of
                Nothing -> object
                    [ "error"   .= ("Failed to parse URI" :: String)
                    , "raw_url" .= url
                    ]
                Just u  ->
                    let auth = uriAuthority u
                    in object
                        [ "scheme"     .= toMaybe (uriScheme u)
                        , "authority"  .= ("EXCLUDE" :: String)
                        , "userinfo"   .= (auth >>= toMaybe . uriUserInfo)
                        , "username"   .= ("EXCLUDE" :: String)
                        , "password"   .= ("EXCLUDE" :: String)
                        , "host"       .= (auth >>= toMaybe . uriRegName)
                        , "port"       .= (auth >>= toMaybe . uriPort)
                        , "path"       .= toMaybe (uriPath u)
                        , "query"      .= toMaybe (uriQuery u)
                        , "query_dict" .= ("EXCLUDE" :: String)
                        , "fragment"   .= toMaybe (uriFragment u)
                        , "raw_url"    .= url
                        ]
        [] ->
            BL.putStrLn (encode (object ["error" .= ("No URL provided" :: String)]))
            >> exitFailure
