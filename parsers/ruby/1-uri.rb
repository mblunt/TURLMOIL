#!/usr/bin/env ruby
# Ruby URL parser using standard URI library
#
# Parses URLs using Ruby's built-in URI module and outputs JSON.

require 'uri'
require 'json'

def parse_url(url_str)
  begin
    uri = URI.parse(url_str)
    
    {
      scheme: uri.scheme&.empty? ? nil : uri.scheme,
      authority: "EXCLUDE",
      userinfo: uri.userinfo&.empty? ? nil : uri.userinfo,
      username: uri.user&.empty? ? nil : uri.user,
      password: uri.password&.empty? ? nil : uri.password,
      host: uri.host&.empty? ? nil : uri.host,
      port: uri.port ? uri.port.to_s : nil,
      path: uri.path&.empty? ? nil : uri.path,
      query: uri.query&.empty? ? nil : uri.query,
      query_dict: uri.query ? URI.decode_www_form(uri.query).to_h : nil,
      fragment: uri.fragment&.empty? ? nil : uri.fragment,
      raw_url: url_str
    }
  rescue => e
    {
      error: e.message,
      raw_url: url_str
    }
  end
end

def main
  if ARGV.length < 1
    puts JSON.generate({ error: "No URL provided" })
    exit 1
  end
  
  url = ARGV[0]
  result = parse_url(url)
  puts JSON.generate(result)
end

if __FILE__ == $0
  main
end