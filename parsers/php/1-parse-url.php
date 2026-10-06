#!/usr/bin/env php
<?php
error_reporting(E_ERROR);
ini_set('display_errors', '0');

// PHP URL parser using parse_url()
//
// Parses URLs using PHP's built-in function and outputs JSON.

function parse_url_custom($url_str) {
    $result = [];
    
    $parsed = @parse_url($url_str);
    
    if ($parsed === false) {
        return [
            'error' => 'Failed to parse URL',
            'raw_url' => $url_str
        ];
    }
    
    $result['scheme'] = isset($parsed['scheme']) && $parsed['scheme'] !== '' ? $parsed['scheme'] : null;
    $result['authority'] = "EXCLUDE"; // parse_url does not provide authority directly
    $result['userinfo'] = "EXCLUDE"; // parse_url does not provide userinfo directly
    $result['username'] = isset($parsed['user']) && $parsed['user'] !== '' ? $parsed['user'] : null;
    $result['password'] = isset($parsed['pass']) && $parsed['pass'] !== '' ? $parsed['pass'] : null;
    $result['host'] = isset($parsed['host']) && $parsed['host'] !== '' ? $parsed['host'] : null;
    $result['port'] = isset($parsed['port']) ? (string)$parsed['port'] : null;
    $result['path'] = isset($parsed['path']) && $parsed['path'] !== '' ? $parsed['path'] : null;
    $result['query'] = isset($parsed['query']) && $parsed['query'] !== '' ? $parsed['query'] : null;
    $result['query_dict'] = null;
    if (isset($parsed['query']) && $parsed['query'] !== '') {
        parse_str($parsed['query'], $query_array);
        $result['query_dict'] = $query_array;
    }
    $result['fragment'] = isset($parsed['fragment']) && $parsed['fragment'] !== '' ? $parsed['fragment'] : null;
    $result['raw_url'] = $url_str;
    
    return $result;
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
