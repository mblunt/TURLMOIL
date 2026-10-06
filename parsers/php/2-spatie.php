#!/usr/bin/env php
<?php
error_reporting(E_ERROR);
ini_set('display_errors', '0');


require_once __DIR__ . '/vendor/autoload.php';

use Spatie\Url\Url;

function parse_url_spatie($url_str) {
    try {
        $url = Url::fromString($url_str);

        $userInfo = $url->getUserInfo();
        $username = "EXCLUDE";
        $password = "EXCLUDE";

        $queryStr = $url->getQuery();
        $queryDict = null;
        if ($queryStr !== '') {
            $queryDict = $url->getAllQueryParameters();
        }

        $port = $url->getPort();

        return [
            'scheme'     => $url->getScheme() !== '' ? $url->getScheme() : null,
            'authority'  => $url->getAuthority() !== '' ? $url->getAuthority() : null,
            'userinfo'   => $userInfo !== '' ? $userInfo : null,
            'username'   => $username,
            'password'   => $password,
            'host'       => $url->getHost() !== '' ? $url->getHost() : null,
            'port'       => $port !== null ? (string)$port : null,
            'path'       => $url->getPath() !== '' ? $url->getPath() : null,
            'query'      => $queryStr !== '' ? $queryStr : null,
            'query_dict' => $queryDict,
            'fragment'   => $url->getFragment() !== '' ? $url->getFragment() : null,
            'raw_url'    => $url_str,
        ];
    } catch (Exception $e) {
        return [
            'error'   => $e->getMessage(),
            'raw_url' => $url_str,
        ];
    }
}

function main() {
    global $argv;

    if (count($argv) < 2) {
        echo json_encode(['error' => 'No URL provided'], JSON_UNESCAPED_SLASHES) . PHP_EOL;
        exit(1);
    }

    $url = $argv[1];
    $result = parse_url_spatie($url);
    echo json_encode($result, JSON_UNESCAPED_SLASHES) . PHP_EOL;
}

if (php_sapi_name() === 'cli') {
    main();
}
