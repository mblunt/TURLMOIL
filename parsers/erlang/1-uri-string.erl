-module(uri_parser).
-export([main/1]).

-define(EXCLUDE, <<"EXCLUDE">>).

null_if_empty(undefined) -> null;
null_if_empty(null) -> null;
null_if_empty(<<>>) -> null;
null_if_empty([]) -> null;
null_if_empty(Value) when is_list(Value) ->
    unicode:characters_to_binary(Value);
null_if_empty(Value) -> Value.

port_to_json(undefined) -> null;
port_to_json(null) -> null;
port_to_json(Value) when is_integer(Value) -> integer_to_binary(Value);
port_to_json(Value) -> null_if_empty(Value).

base_output(RawUrl, Error) ->
    #{
        <<"scheme">> => null,
        <<"authority">> => ?EXCLUDE,
        <<"userinfo">> => null,
        <<"username">> => ?EXCLUDE,
        <<"password">> => ?EXCLUDE,
        <<"host">> => null,
        <<"port">> => null,
        <<"path">> => null,
        <<"query">> => null,
        <<"query_dict">> => ?EXCLUDE,
        <<"fragment">> => null,
        <<"raw_url">> => RawUrl,
        <<"error">> => Error
    }.

parse_url(RawUrl) ->
    case uri_string:parse(RawUrl) of
        {error, Atom, _Rest} ->
            base_output(RawUrl, atom_to_binary(Atom));
        ParsedMap when is_map(ParsedMap) ->
            Out0 = base_output(RawUrl, null),
            Out0#{
                <<"scheme">> => null_if_empty(maps:get(scheme, ParsedMap, undefined)),
                <<"userinfo">> => null_if_empty(maps:get(userinfo, ParsedMap, undefined)),
                <<"host">> => null_if_empty(maps:get(host, ParsedMap, undefined)),
                <<"port">> => port_to_json(maps:get(port, ParsedMap, undefined)),
                <<"path">> => null_if_empty(maps:get(path, ParsedMap, undefined)),
                <<"query">> => null_if_empty(maps:get(query, ParsedMap, undefined)),
                <<"fragment">> => null_if_empty(maps:get(fragment, ParsedMap, undefined))
            }
    end.

handle_client(Client) ->
    case gen_tcp:recv(Client, 0, 30000) of
        {ok, Data} ->
            RawUrl = unicode:characters_to_binary(string:trim(Data)),
            Result = if
                byte_size(RawUrl) =:= 0 -> base_output(null, <<"empty url">>);
                true -> parse_url(RawUrl)
            end,
            Json = json:encode(Result),
            gen_tcp:send(Client, [Json, <<"\n">>]);
        {error, _} -> ok
    end,
    gen_tcp:close(Client).

accept_loop(ListenSocket) ->
    {ok, Client} = gen_tcp:accept(ListenSocket),
    spawn(fun() -> handle_client(Client) end),
    accept_loop(ListenSocket).

start_server(Port) ->
    {ok, ListenSocket} = gen_tcp:listen(Port, [binary, {packet, line}, {active, false}, {reuseaddr, true}]),
    io:format("Erlang uri_string server ready on port ~p~n", [Port]),
    accept_loop(ListenSocket).

main(["--server", PortStr]) ->
    Port = list_to_integer(PortStr),
    start_server(Port);

main([RawUrlList]) ->
    RawUrl = unicode:characters_to_binary(RawUrlList),
    Json = json:encode(parse_url(RawUrl)),
    io:format("~s~n", [Json]),
    erlang:halt(0);

main([]) ->
    Json = json:encode(base_output(null, <<"No URL provided">>)),
    io:format("~s~n", [Json]),
    erlang:halt(0);

main(_) ->
    Json = json:encode(base_output(null, <<"Usage: pass exactly one URL as an argument">>)),
    io:format("~s~n", [Json]),
    erlang:halt(0).
