#!/usr/bin/env perl
use strict;
use warnings;

use Mojo::URL;
use JSON;

sub parse_url {
    my ($url_str) = @_;

    my %result = (
        scheme     => undef,
        authority  => undef,
        userinfo   => undef,
        username   => undef,
        password   => undef,
        host       => undef,
        port       => undef,
        path       => undef,
        query      => undef,
        query_dict => undef,
        fragment   => undef,
        raw_url    => $url_str,
        error      => undef,
    );

    eval {
        my $url = Mojo::URL->new($url_str);

        $result{scheme} = $url->scheme;

        # Mojo::URL doesn't provide a single "authority" getter; avoid reconstructing.
        $result{authority} = 'EXCLUDE';

        my $userinfo = $url->userinfo;
        if (defined $userinfo && length $userinfo) {
            $result{userinfo} = $userinfo;
        }

        my $user = $url->username;
        if (defined $user && length $user) {
            $result{username} = $user;
        }

        my $pass = $url->password;
        if (defined $pass && length $pass) {
            $result{password} = $pass;
        }

        my $host = $url->host;
        if (defined $host && length $host) {
            $result{host} = $host;
        }

        my $port = $url->port;
        if (defined $port && length $port) {
            $result{port} = $port;
        }

        my $path = $url->path->to_string;
        if (defined $path && length $path) {
            $result{path} = $path;
        }

        my $query = $url->query->to_string;
        if (defined $query && length $query) {
            $result{query} = $query;
        }

        $result{query_dict} = 'EXCLUDE';

        my $fragment = $url->fragment;
        if (defined $fragment && length $fragment) {
            $result{fragment} = $fragment;
        }
    };

    if ($@) {
        $result{error} = "$@";
    }

    return \%result;
}

sub main {
    my $url = $ARGV[0];

    if (!$url) {
        my $result = parse_url('');
        $result->{error} = 'No URL provided';
        print JSON->new->canonical->encode($result);
        exit 1;
    }

    my $result = parse_url($url);
    print JSON->new->canonical->encode($result);
}

main() unless caller;
