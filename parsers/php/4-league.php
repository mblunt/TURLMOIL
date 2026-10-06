#!/usr/bin/env php
<?php
error_reporting(E_ERROR);
ini_set('display_errors', '0');


require_once __DIR__ . '/vendor/autoload.php';

use League\Uri\Uri;

function parse_url_league($url_str) {
    try {
        $url = Uri::new($url_str);

        $queryStr = $url->getQuery();

        $port = $url->getPort();
        $userInfo = $url->getUserInfo();
        $authority = $url->getAuthority();
        $scheme = $url->getScheme();
        $host = $url->getHost();
        $path = $url->getPath();
        $fragment = $url->getFragment();

        return [
            'scheme'     => $scheme !== '' && $scheme !== null ? $scheme : null,
            'authority'  => $authority !== '' && $authority !== null ? $authority : null,
            'userinfo'   => $userInfo !== '' && $userInfo !== null ? $userInfo : null,
            'username'   => "EXCLUDE",
            'password'   => "EXCLUDE",
            'host'       => $host !== '' && $host !== null ? $host : null,
            'port'       => $port !== null ? (string)$port : null,
            'path'       => $path !== '' && $path !== null ? $path : null,
            'query'      => $queryStr !== '' && $queryStr !== null ? $queryStr : null,
            'query_dict' => "EXCLUDE",
            'fragment'   => $fragment !== '' && $fragment !== null ? $fragment : null,
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
    $result = parse_url_league($url);
    echo json_encode($result, JSON_UNESCAPED_SLASHES) . PHP_EOL;
}

if (php_sapi_name() === 'cli') {
    main();
}
