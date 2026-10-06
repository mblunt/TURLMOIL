// https://pub.dev/packages/uri

// Does not work because template must be predefined.
// root@04a20d8994be:/parsers/dart# ./2-uri test
// {"error":"ParseException: {scheme}://{host}{path}{?query}{#fragment} does not match test","raw_url":"test"}
// root@04a20d8994be:/parsers/dart# 

import 'package:uri/uri.dart';
import 'dart:convert' show jsonEncode;

Map<String, dynamic> parseUrl(String url) {
  try {
    final uri = Uri.parse(url);

    // Create a URI template pattern to match the parsed URI structure
    final template = UriTemplate('{scheme}://{host}{path}{?query}{#fragment}');
    final parser = UriParser(template);

    final params = parser.parse(uri);

    return {
      'scheme': params['scheme'] ?? null,
      'authority': uri.authority.isNotEmpty ? uri.authority : null,
      'userinfo': 'EXCLUDE',
      'username': 'EXCLUDE',
      'password': 'EXCLUDE',
      'host': params['host'] ?? null,
      'port': uri.hasPort ? uri.port.toString() : null,
      'path': params['path'] ?? null,
      'query': params['query'] ?? null,
      'query_dict': 'EXCLUDE',
      'fragment': params['fragment'] ?? null,
      'raw_url': url,
    };
  } catch (e) {
    return {
      'error': e.toString(),
      'raw_url': url,
    };
  }
}

void main(List<String> args) {
  if (args.isEmpty) {
    print(jsonEncode({'error': 'No URL provided'}));
    return;
  }

  final url = args[0];
  final result = parseUrl(url);
  print(jsonEncode(result));
}