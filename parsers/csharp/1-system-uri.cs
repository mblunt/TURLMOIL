// nuget: Newtonsoft.Json,13.0.3
using System;
using System.Web;
using System.Collections.Generic;
using System.Linq;
using Newtonsoft.Json;

if (args.Length < 1) {
    Console.WriteLine(JsonConvert.SerializeObject(new { error = "No URL provided" }));
    Environment.Exit(1);
}

Console.WriteLine(JsonConvert.SerializeObject(ParseUrl(args[0])));

static URLResult ParseUrl(string urlStr)
{
    var result = new URLResult { raw_url = urlStr };
    try
    {
        var uri = new Uri(urlStr);

        result.scheme = uri.Scheme;
        result.authority = uri.Authority;
        result.userinfo = string.IsNullOrEmpty(uri.UserInfo) ? null : uri.UserInfo;
        result.host = uri.Host;
        result.port = uri.Port.ToString();
        result.path = uri.AbsolutePath;
        result.query = uri.Query;
        result.fragment = uri.Fragment;

        var nvc = HttpUtility.ParseQueryString(uri.Query);
        result.query_dict = nvc.AllKeys
            .Where(k => k != null)
            .ToDictionary(k => k!, k => nvc.GetValues(k)!);


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
    public Dictionary<string, string[]>? query_dict { get; set; }
    public string? fragment { get; set; }
    public string? raw_url { get; set; }
    public string? error { get; set; }
}
