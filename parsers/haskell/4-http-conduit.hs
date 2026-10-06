{-# LANGUAGE OverloadedStrings #-}

-- Signal: http-conduit, 352 reverse deps. The standard streaming HTTP client
-- in the Haskell ecosystem; selected because parseRequest is the entry point
-- most application code uses when constructing outbound requests from URL
-- strings, and it applies its own normalisation on top of http-client.
-- Note: http-conduit re-exports parseRequest from http-client; including it
-- separately ensures its own version pinning is exercised.

import Network.HTTP.Conduit (parseRequest, Request(..))
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
                -- path includes leading '/', queryString includes leading '?'
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