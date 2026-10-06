(ns parser.core
  (:require [lambdaisland.uri :as uri]
            [clojure.data.json :as json])
  (:gen-class))

(defn -main [& args]
  (when (empty? args)
    (println (json/write-str {"error" "No URL provided"}))
    (System/exit 1))
  (let [raw-url (first args)]
    (try
      (let [parsed   (uri/uri raw-url)
            port-raw (:port parsed)
            q-str    (:query parsed)
            q-map    (when (some? q-str)
                       (try (uri/query-map parsed)
                            (catch Exception _ nil)))]
        (println
         (json/write-str
          {"scheme"     (:scheme parsed)
           "authority"  "EXCLUDE"
           "userinfo"   "EXCLUDE"
           "username"   (:user parsed)
           "password"   (:password parsed)
           "host"       (:host parsed)
           "port"       (when (some? port-raw) (str port-raw))
           "path"       (:path parsed)
           "query"      q-str
           "query_dict" q-map
           "fragment"   (:fragment parsed)
           "raw_url"    raw-url})))
      (catch Exception e
        (println (json/write-str {"error" (.getMessage e) "raw_url" raw-url}))))))
