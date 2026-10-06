#!/usr/bin/env php
<?php
error_reporting(E_ERROR);
ini_set('display_errors', '0');


require_once __DIR__ . '/vendor/autoload.php';

use Laminas\Uri\UriFactory;

function parse_url_custom($url_str) {
    try {
        $uri = UriFactory::factory($url_str);
        
        return [
            'scheme' => $uri->getScheme() ?: null,
            'authority' => "EXCLUDE", // Laminas URI does not provide authority directly
            'userinfo' => $uri->getUserInfo() ?: null,
            'username' => "EXCLUDE", // Laminas URI does not provide username directly
            'password' => "EXCLUDE", // Laminas URI does not provide password directly
            'host' => $uri->getHost() ?: null,
            'port' => $uri->getPort() ? (string)$uri->getPort() : null,
            'path' => $uri->getPath() ?: null,
            'query' => $uri->getQuery() ?: null,
            'query_dict' => $uri->getQueryAsArray() ?: null,
            'fragment' => $uri->getFragment() ?: null,
            'raw_url' => $url_str
        ];
    } catch (\Throwable $e) {
        return [
            'error' => $e->getMessage(),
            'raw_url' => $url_str
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
    $result = parse_url_custom($url);
    echo json_encode($result, JSON_UNESCAPED_SLASHES) . PHP_EOL;
}

if (php_sapi_name() === 'cli') {
    main();
}
