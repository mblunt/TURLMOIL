#!/usr/bin/env php
<?php
error_reporting(E_ERROR);
ini_set('display_errors', '0');

require_once __DIR__ . '/vendor/autoload.php';

function parse_url_sabre($url_str) {
    try {
        $parts = Sabre\Uri\parse($url_str);

        return [
            'scheme'     => $parts['scheme'],
            'authority'  => "EXCLUDE",
            'userinfo'   => "EXCLUDE",
            'username'   => $parts['user'],
            'password'   => $parts['pass'],
            'host'       => $parts['host'],
            'port'       => $parts['port'] !== null ? (string)$parts['port'] : null,
            'path'       => $parts['path'] !== '' ? $parts['path'] : null,
            'query'      => $parts['query'],
            'query_dict' => "EXCLUDE",
            'fragment'   => $parts['fragment'],
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
    $result = parse_url_sabre($url);
    echo json_encode($result, JSON_UNESCAPED_SLASHES) . PHP_EOL;
}

if (php_sapi_name() === 'cli') {
    main();
}
?>
