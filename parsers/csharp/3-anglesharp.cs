// nuget: AngleSharp,1.4.0
using System;
using System.Text.Json;
using AngleSharp.Dom;

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

        if (url.IsInvalid)
        {
            result.error = "Invalid URL";
            return result;
        }

        result.scheme    = string.IsNullOrEmpty(url.Scheme)   ? null : url.Scheme;
        result.authority = "EXCLUDE";
        result.userinfo  = "EXCLUDE";
        result.username  = string.IsNullOrEmpty(url.UserName) ? null : url.UserName;
        result.password  = string.IsNullOrEmpty(url.Password) ? null : url.Password;
        result.host      = string.IsNullOrEmpty(url.HostName) ? null : url.HostName;
        result.port      = string.IsNullOrEmpty(url.Port)     ? null : url.Port;
        result.path      = string.IsNullOrEmpty(url.PathName) ? null : url.PathName;
        result.query     = url.Search;
        result.fragment  = url.Hash;
        result.query_dict = "EXCLUDE";
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
    public object? query_dict { get; set; }
    public string? fragment { get; set; }
    public string? raw_url { get; set; }
    public string? error { get; set; }
}
