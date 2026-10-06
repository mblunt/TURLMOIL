{-# LANGUAGE OverloadedStrings #-}

-- Signal: uri-bytestring, 46 reverse deps. RFC 3986 parser using ByteString
-- for efficiency; preferred in performance-sensitive code (servant-client,
-- OAuth/JWT libraries).
--
-- The library splits userinfo into (uiUsername, uiPassword) — no combined
-- userinfo string is provided, so userinfo is EXCLUDE.
-- The library stores query as parsed pairs only — no raw query string,
-- so query is EXCLUDE and query_dict comes from queryPairs.
-- authority is EXCLUDE — not provided as a string, only as components.

import URI.ByteString
import Data.Aeson (encode, object, (.=))
import qualified Data.Aeson.Key as AK
import qualified Data.ByteString.Char8 as BS
import qualified Data.ByteString.Lazy.Char8 as BL
import System.Environment (getArgs)
import System.Exit (exitFailure)

bs2s :: BS.ByteString -> String
bs2s = BS.unpack

toMaybe :: String -> Maybe String
toMaybe "" = Nothing
toMaybe s  = Just s

main :: IO ()
main = do
    args <- getArgs
    case args of
        (url:_) ->
            BL.putStrLn $ encode $
                case parseURI laxURIParserOptions (BS.pack url) of
                    Left err -> object
                        [ "error"   .= show err
                        , "raw_url" .= url
                        ]
                    Right u  ->
                        let auth   = uriAuthority u
                            ui     = auth >>= authorityUserInfo
                            uname  = fmap (toMaybe . bs2s . uiUsername) ui >>= id
                            passwd = fmap (toMaybe . bs2s . uiPassword) ui >>= id
                            host   = fmap (toMaybe . bs2s . hostBS . authorityHost) auth >>= id
                            port   = fmap (show . portNumber) (auth >>= authorityPort)
                            Scheme schBS = uriScheme u
                            scheme = toMaybe (bs2s schBS)
                            path   = toMaybe . bs2s $ uriPath u
                            pairs  = queryPairs (uriQuery u)
                            qdict  = if null pairs then Nothing
                                     else Just . object $
                                          [ AK.fromString (bs2s k) .= bs2s v
                                          | (k, v) <- pairs ]
                            frag   = uriFragment u >>= toMaybe . bs2s
                        in object
                            [ "scheme"     .= scheme
                            , "authority"  .= ("EXCLUDE" :: String)
                            , "userinfo"   .= ("EXCLUDE" :: String)
                            , "username"   .= uname
                            , "password"   .= passwd
                            , "host"       .= host
                            , "port"       .= port
                            , "path"       .= path
                            , "query"      .= ("EXCLUDE" :: String)
                            , "query_dict" .= qdict
                            , "fragment"   .= frag
                            , "raw_url"    .= url
                            ]
        [] ->
            BL.putStrLn (encode (object ["error" .= ("No URL provided" :: String)]))
            >> exitFailure