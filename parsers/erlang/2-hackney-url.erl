-module(hackney_url_parser).
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
port_to_json(0) -> null;
port_to_json(Value) when is_integer(Value) -> integer_to_binary(Value);
port_to_json(Value) -> null_if_empty(Value).

base_output(RawUrl, Error) ->
    #{
        <<"scheme">> => null,
        <<"authority">> => ?EXCLUDE,
        <<"userinfo">> => ?EXCLUDE,
        <<"username">> => null,
        <<"password">> => null,
        <<"host">> => null,
        <<"port">> => null,
        <<"path">> => null,
        <<"query">> => null,
        <<"query_dict">> => ?EXCLUDE,
        <<"fragment">> => null,
        <<"raw_url">> => RawUrl,
        <<"error">> => Error
    }.

setup_code_path() ->
    Paths = filelib:wildcard("/opt/hackney/_build/default/lib/*/ebin"),
    lists:foreach(fun(P) -> code:add_patha(P) end, Paths),
    ok.

scheme_to_binary(undefined) -> null;
scheme_to_binary(Scheme) when is_atom(Scheme) -> atom_to_binary(Scheme, utf8);
scheme_to_binary(Scheme) -> null_if_empty(Scheme).

error_to_binary(Reason) ->
    unicode:characters_to_binary(io_lib:format("~p", [Reason])).

parse_url(RawUrl) ->
    try
        Url = hackney_url:parse_url(RawUrl),
        Out0 = base_output(RawUrl, null),
        Out0#{
            <<"scheme">> => scheme_to_binary(hackney_url:property(scheme, Url)),
            <<"username">> => null_if_empty(hackney_url:property(user, Url)),
            <<"password">> => null_if_empty(hackney_url:property(password, Url)),
            <<"host">> => null_if_empty(hackney_url:property(host, Url)),
            <<"port">> => port_to_json(hackney_url:property(port, Url)),
            <<"path">> => null_if_empty(hackney_url:property(path, Url)),
            <<"query">> => null_if_empty(hackney_url:property(qs, Url)),
            <<"fragment">> => null_if_empty(hackney_url:property(fragment, Url))
        }
    catch
        Class:Reason ->
            base_output(RawUrl, <<(atom_to_binary(Class, utf8))/binary, ":", (error_to_binary(Reason))/binary>>)
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
    setup_code_path(),
    {ok, ListenSocket} = gen_tcp:listen(Port, [binary, {packet, line}, {active, false}, {reuseaddr, true}]),
    io:format("Erlang hackney_url server ready on port ~p~n", [Port]),
    accept_loop(ListenSocket).

main(["--server", PortStr]) ->
    Port = list_to_integer(PortStr),
    start_server(Port);

main([RawUrlList]) ->
    setup_code_path(),
    RawUrl = unicode:characters_to_binary(RawUrlList),
    io:format("~s~n", [json:encode(parse_url(RawUrl))]),
    erlang:halt(0);

main([]) ->
    io:format("~s~n", [json:encode(base_output(null, <<"No URL provided">>))]),
    erlang:halt(0);

main(_) ->
    io:format("~s~n", [json:encode(base_output(null, <<"Usage: pass exactly one URL as an argument">>))]),
    erlang:halt(0).
