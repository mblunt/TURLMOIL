// https://api.dart.dev/stable/latest/dart-core/

import 'dart:convert' show jsonEncode;

Map<String, dynamic> parseUrl(String url) {
  try {
    final uri = Uri.parse(url);

    return {
      'scheme': uri.scheme.isNotEmpty ? uri.scheme : null,
      'authority': uri.authority.isNotEmpty ? uri.authority : null,
      'userinfo': 'EXCLUDE',
      'username': 'EXCLUDE',
      'password': 'EXCLUDE',
      'host': uri.host.isNotEmpty ? uri.host : null,
      'port': uri.hasPort ? uri.port.toString() : null,
      'path': uri.path.isNotEmpty ? uri.path : null,
      'query': uri.query.isNotEmpty ? uri.query : null,
      'query_dict': 'EXCLUDE',
      'fragment': uri.fragment.isNotEmpty ? uri.fragment : null,
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