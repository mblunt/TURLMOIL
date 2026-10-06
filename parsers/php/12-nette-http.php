#!/usr/bin/env php
<?php
error_reporting(E_ERROR);
ini_set('display_errors', '0');


require_once __DIR__ . '/vendor/autoload.php';

use Nette\Http\UrlImmutable;

function parse_url_nette($url_str) {
    try {
        $url = new UrlImmutable($url_str);

        $scheme   = $url->getScheme();
        $user     = $url->getUser();
        $pass     = $url->getPassword();
        $host     = $url->getHost();
        $port     = $url->getPort();
        $path     = $url->getPath();
        $query    = $url->getQuery();
        $fragment = $url->getFragment();

        return [
            'scheme'     => $scheme !== '' && $scheme !== null ? $scheme : null,
            'authority'  => "EXCLUDE",
            'userinfo'   => "EXCLUDE",
            'username'   => $user !== '' && $user !== null ? $user : null,
            'password'   => $pass !== '' && $pass !== null ? $pass : null,
            'host'       => $host !== '' && $host !== null ? $host : null,
            'port'       => ($port !== null && $port !== 0) ? (string)$port : null,
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
    $result = parse_url_nette($url);
    echo json_encode($result, JSON_UNESCAPED_SLASHES) . PHP_EOL;
}

if (php_sapi_name() === 'cli') {
    main();
}
