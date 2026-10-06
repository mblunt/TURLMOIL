#!/usr/bin/env go run
// Go URL parser using net/url
//
// Parses URLs using Go's standard library and outputs JSON.

package main

import (
	"encoding/json"
	"fmt"
	"net/url"
	"os"
)

type URLResult struct {
	Scheme   *string `json:"scheme"`
	Authority *string `json:"authority"`
	Userinfo *string `json:"userinfo"`
	Username *string `json:"username"`
	Password *string `json:"password"`
	Host     *string `json:"host"`
	Port     *string `json:"port"`
	Path     *string `json:"path"`
	Query    *string `json:"query"`
	QueryDict map[string][]string `json:"query_dict"`
	Fragment *string `json:"fragment"`
	RawURL   string  `json:"raw_url"`
	Error    *string `json:"error,omitempty"`
}

func stringPtr(s string) *string {
	if s == "" {
		return nil
	}
	return &s
}

func parseURL(urlStr string) URLResult {
	result := URLResult{RawURL: urlStr}

	parsedURL, err := url.Parse(urlStr)
	if err != nil {
		errMsg := err.Error()
		result.Error = &errMsg
		return result
	}

	result.Scheme = stringPtr(parsedURL.Scheme)
	result.Authority = stringPtr("EXCLUDE") // net/url does not provide authority directly
	
	// Userinfo
	if parsedURL.User != nil {
		result.Userinfo = stringPtr(parsedURL.User.String())
	} else {
		result.Userinfo = nil
	}

	// Username
	if parsedURL.User != nil {
		result.Username = stringPtr(parsedURL.User.Username())
	} else {
		result.Username = nil
	}

	// Password
	if parsedURL.User != nil {
		if password, ok := parsedURL.User.Password(); ok {
			result.Password = stringPtr(password)
		} else {
			result.Password = nil
		}
	} else {
		result.Password = nil
	}

	result.Host = stringPtr(parsedURL.Hostname())
	result.Port = stringPtr(parsedURL.Port())
	result.Path = stringPtr(parsedURL.Path)
	result.Query = stringPtr(parsedURL.RawQuery)

	// Query Dict
	result.QueryDict = parsedURL.Query()

	result.Fragment = stringPtr(parsedURL.Fragment)

	return result
}

func main() {
	if len(os.Args) < 2 {
		errorResult := map[string]string{"error": "No URL provided"}
		jsonOutput, _ := json.Marshal(errorResult)
		fmt.Println(string(jsonOutput))
		os.Exit(1)
	}

	urlStr := os.Args[1]
	result := parseURL(urlStr)
	jsonOutput, _ := json.Marshal(result)
	fmt.Println(string(jsonOutput))
}
