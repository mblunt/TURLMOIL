{-# LANGUAGE OverloadedStrings #-}

-- Signal: http-client, 704 reverse deps. The foundational Haskell HTTP client
-- engine that underlies http-conduit, wreq, and req; selected because
-- parseRequest is the canonical URL-to-Request conversion used by almost
-- every Haskell HTTP client library and applies host/port/path normalisation
-- directly on the URL string.

import Network.HTTP.Client (parseRequest, Request(..))
import Control.Exception (try, SomeException, evaluate)
import Data.Aeson (encode, object, (.=), Value)
import qualified Data.ByteString.Char8 as BS
import qualified Data.ByteString.Lazy.Char8 as BL
import System.Environment (getArgs)
import System.Exit (exitFailure)

bs2s :: BS.ByteString -> String
bs2s = BS.unpack

toMaybe :: String -> Maybe String
toMaybe "" = Nothing
toMaybe s  = Just s

parseUrl :: String -> IO Value
parseUrl url = do
    result <- try (evaluate =<< parseRequest url) :: IO (Either SomeException Request)
    return $ case result of
        Left err -> object ["error" .= show err, "raw_url" .= url]
        Right req ->
            let hostStr   = bs2s (host req)
                portNum   = show (port req)
                pathStr   = toMaybe (bs2s (path req))
                rawQS     = queryString req
                queryStr  = if BS.null rawQS then Nothing
                            else toMaybe (bs2s rawQS)
            in object
                [ "scheme"     .= ("EXCLUDE" :: String)
                , "authority"  .= ("EXCLUDE" :: String)
                , "userinfo"   .= ("EXCLUDE" :: String)
                , "username"   .= ("EXCLUDE" :: String)
                , "password"   .= ("EXCLUDE" :: String)
                , "host"       .= toMaybe hostStr
                , "port"       .= toMaybe portNum
                , "path"       .= pathStr
                , "query"      .= queryStr
                , "query_dict" .= ("EXCLUDE" :: String)
                , "fragment"   .= ("EXCLUDE" :: String)
                , "raw_url"    .= url
                ]

main :: IO ()
main = do
    args <- getArgs
    case args of
        (u:_) -> parseUrl u >>= BL.putStrLn . encode
        []    -> BL.putStrLn (encode (object ["error" .= ("No URL provided" :: String)])) >> exitFailure