#!/usr/bin/env php
<?php
error_reporting(E_ERROR);
ini_set('display_errors', '0');


require_once __DIR__ . '/vendor/autoload.php';

use Opis\Uri\Uri;

function parse_url_opis($url_str) {
    try {
        $url = Uri::create($url_str);

        if ($url === null) {
            return [
                'error'   => 'Failed to parse URL',
                'raw_url' => $url_str,
            ];
        }

        $scheme    = $url->scheme();
        $authority = $url->authority();
        $userInfo  = $url->userInfo();
        $host      = $url->host();
        $port      = $url->port();
        $path      = $url->path();
        $query     = $url->query();
        $fragment  = $url->fragment();

        return [
            'scheme'     => $scheme !== '' && $scheme !== null ? $scheme : null,
            'authority'  => $authority !== '' && $authority !== null ? $authority : null,
            'userinfo'   => $userInfo !== '' && $userInfo !== null ? $userInfo : null,
            'username'   => "EXCLUDE",
            'password'   => "EXCLUDE",
            'host'       => $host !== '' && $host !== null ? $host : null,
            'port'       => $port !== null ? (string)$port : null,
            'path'       => $path !== '' && $path !== null ? $path : null,
            'query'      => $query !== '' && $query !== null ? $query : null,
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
    $result = parse_url_opis($url);
    echo json_encode($result, JSON_UNESCAPED_SLASHES) . PHP_EOL;
}

if (php_sapi_name() === 'cli') {
    main();
}
