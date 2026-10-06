#!/usr/bin/env perl
use strict;
use warnings;

use URI;
use URI::QueryParam; 
use JSON;

sub parse_url {
    my ($url_str) = @_;
    my %result;
    
    eval {
        # Create the URI object
        my $uri = URI->new($url_str);
        
        # Standard components
        $result{scheme}    = $uri->scheme;
        $result{authority} = $uri->can('authority') ? $uri->authority : undef;
        $result{userinfo}  = $uri->can('userinfo')  ? $uri->userinfo  : undef;

        # We clone the URI and set it to 'ftp' because URI::ftp implements 
        # the user() and password() methods natively, unlike URI::http.
        if (defined $result{userinfo}) {
            my $temp_uri = $uri->clone;
            $temp_uri->scheme('ftp'); 
            $result{username} = $temp_uri->can('user')     ? $temp_uri->user     : undef;
            $result{password} = $temp_uri->can('password') ? $temp_uri->password : undef;
        } else {
            $result{username} = undef;
            $result{password} = undef;
        }
        # ------------------------------------

        $result{host}      = $uri->can('host')      ? $uri->host      : undef;
        $result{port}      = $uri->can('port')      ? $uri->port      : undef;
        $result{path}      = $uri->can('path')      ? $uri->path      : undef;
        $result{query}     = $uri->can('query')     ? $uri->query     : undef;
        $result{query_dict}= $uri->can('query_form_hash') ? $uri->query_form_hash : undef;
        $result{fragment}  = $uri->can('fragment')  ? $uri->fragment  : undef;
        $result{raw_url}   = $url_str;
    };
    
    if ($@) {
        $result{error}   = "$@";
        $result{raw_url} = $url_str;
    }
    
    return \%result;
}

sub main {
    my $url = $ARGV[0];
    
    if (!$url) {
        # Note: Using STDERR for the error message so it doesn't pollute JSON output
        warn "No URL provided.\n";
        exit 1;
    }
    
    my $result = parse_url($url);
    print JSON->new->canonical->pretty->encode($result);
}

main() unless caller;