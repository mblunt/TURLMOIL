// nuget: Flurl,4.0.0
using System;
using System.Text.Json;
using System.Collections.Generic;
using System.Linq;
using Flurl;

if (args.Length < 1)
{
    Console.WriteLine(JsonSerializer.Serialize(new { error = "No URL provided" }));
    Environment.Exit(1);
}

Console.WriteLine(JsonSerializer.Serialize(ParseUrl(args[0])));

static URLResult ParseUrl(string urlStr)
{
    var result = new URLResult { raw_url = urlStr };

    try
    {
        var url = new Url(urlStr);

        result.scheme = string.IsNullOrEmpty(url.Scheme) ? null : url.Scheme;
        result.authority = string.IsNullOrEmpty(url.Authority) ? null : url.Authority;
        result.userinfo = string.IsNullOrEmpty(url.UserInfo) ? null : url.UserInfo;
        result.host = string.IsNullOrEmpty(url.Host) ? null : url.Host;
        result.port = url.Port?.ToString();
        result.path = string.IsNullOrEmpty(url.Path) ? null : url.Path;
        result.query = string.IsNullOrEmpty(url.Query) ? null : url.Query;
        result.fragment = string.IsNullOrEmpty(url.Fragment) ? null : url.Fragment;

        result.query_dict = url.QueryParams
            .GroupBy(p => p.Name)
            .ToDictionary(
                g => g.Key,
                g => g.Select(p => p.Value?.ToString() ?? "").ToList()
            );

        result.username = "EXCLUDE";
        result.password = "EXCLUDE";
    }
    catch (Exception e)
    {
        result.error = e.Message;
    }

    return result;
}

class URLResult
{
    public string? scheme { get; set; }
    public string? authority { get; set; }
    public string? userinfo { get; set; }
    public string? username { get; set; }
    public string? password { get; set; }
    public string? host { get; set; }
    public string? port { get; set; }
    public string? path { get; set; }
    public string? query { get; set; }
    public Dictionary<string, List<string>>? query_dict { get; set; }
    public string? fragment { get; set; }
    public string? raw_url { get; set; }
    public string? error { get; set; }
}
