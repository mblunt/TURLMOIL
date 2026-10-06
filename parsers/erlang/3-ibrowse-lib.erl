-module(ibrowse_url_parser).
-export([main/1]).

-define(EXCLUDE, <<"EXCLUDE">>).

-record(url, {
    abspath,
    host,
    port,
    username,
    password,
    path,
    protocol,
    host_type
}).

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
        <<"query">> => ?EXCLUDE,
        <<"query_dict">> => ?EXCLUDE,
        <<"fragment">> => ?EXCLUDE,
        <<"raw_url">> => RawUrl,
        <<"error">> => Error
    }.

setup_code_path() ->
    Paths = filelib:wildcard("/opt/ibrowse/_build/default/lib/*/ebin"),
    lists:foreach(fun(P) -> code:add_patha(P) end, Paths),
    ok.

scheme_to_binary(undefined) -> null;
scheme_to_binary(Scheme) when is_atom(Scheme) -> atom_to_binary(Scheme, utf8);
scheme_to_binary(Scheme) -> null_if_empty(Scheme).

error_to_binary(Reason) ->
    unicode:characters_to_binary(io_lib:format("~p", [Reason])).

parse_url(RawUrlList, RawUrlBin) ->
    try
        case ibrowse_lib:parse_url(RawUrlList) of
            #url{} = UrlRec ->
                Out0 = base_output(RawUrlBin, null),
                Out0#{
                    <<"scheme">> => scheme_to_binary(UrlRec#url.protocol),
                    <<"username">> => null_if_empty(UrlRec#url.username),
                    <<"password">> => null_if_empty(UrlRec#url.password),
                    <<"host">> => null_if_empty(UrlRec#url.host),
                    <<"port">> => port_to_json(UrlRec#url.port),
                    <<"path">> => null_if_empty(UrlRec#url.path)
                };
            {error, ParseReason} ->
                base_output(RawUrlBin, error_to_binary(ParseReason));
            Other ->
                base_output(RawUrlBin, error_to_binary({unexpected_return, Other}))
        end
    catch
        Class:CatchReason ->
            base_output(RawUrlBin, <<(atom_to_binary(Class, utf8))/binary, ":", (error_to_binary(CatchReason))/binary>>)
    end.

handle_client(Client) ->
    case gen_tcp:recv(Client, 0, 30000) of
        {ok, Data} ->
            Trimmed = string:trim(binary_to_list(Data)),
            RawUrlBin = unicode:characters_to_binary(Trimmed),
            Result = if
                length(Trimmed) =:= 0 -> base_output(null, <<"empty url">>);
                true -> parse_url(Trimmed, RawUrlBin)
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
    io:format("Erlang ibrowse_lib server ready on port ~p~n", [Port]),
    accept_loop(ListenSocket).

main(["--server", PortStr]) ->
    Port = list_to_integer(PortStr),
    start_server(Port);

main([RawUrlList]) ->
    setup_code_path(),
    RawUrlBin = unicode:characters_to_binary(RawUrlList),
    io:format("~s~n", [json:encode(parse_url(RawUrlList, RawUrlBin))]),
    erlang:halt(0);

main([]) ->
    io:format("~s~n", [json:encode(base_output(null, <<"No URL provided">>))]),
    erlang:halt(0);

main(_) ->
    io:format("~s~n", [json:encode(base_output(null, <<"Usage: pass exactly one URL as an argument">>))]),
    erlang:halt(0).
