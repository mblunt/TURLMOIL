Code.put_compiler_option(:ignore_module_conflict, true)
defmodule URLParser do
  def main(args) do
    args = Enum.drop_while(args, &(&1 == "--"))
    case args do
      ["--server", port_str | _] ->
        start_server(String.to_integer(port_str))

      [] ->
        IO.puts(Jason.encode!(%{error: "No URL provided"}))
        System.halt(1)

      [url | _] ->
        IO.puts(Jason.encode!(parse_url(url)))
    end
  end

  def parse_url(url_str) do
    case URL.new(url_str) do
      {:ok, parsed} ->
        %{
          scheme:     empty_to_nil(parsed.scheme),
          authority:  "EXCLUDE",
          userinfo:   empty_to_nil(parsed.userinfo),
          username:   "EXCLUDE",
          password:   "EXCLUDE",
          host:       empty_to_nil(parsed.host),
          port:       if(parsed.port, do: to_string(parsed.port), else: nil),
          path:       empty_to_nil(parsed.path),
          query:      empty_to_nil(parsed.query),
          query_dict: "EXCLUDE",
          fragment:   empty_to_nil(parsed.fragment),
          raw_url:    url_str
        }

      {:error, {_exception, reason}} ->
        %{error: inspect(reason), raw_url: url_str}
    end
  rescue
    e -> %{error: Exception.message(e), raw_url: url_str}
  end

  def start_server(port) do
    {:ok, listen_socket} = :gen_tcp.listen(port, [
      :binary, packet: :line, active: false, reuseaddr: true
    ])
    accept_loop(listen_socket)
  end

  defp accept_loop(listen_socket) do
    {:ok, client} = :gen_tcp.accept(listen_socket)
    spawn(fn -> handle_client(client) end)
    accept_loop(listen_socket)
  end

  defp handle_client(client) do
    case :gen_tcp.recv(client, 0, 30_000) do
      {:ok, data} ->
        url = String.trim(data)
        response =
          if url == "" do
            Jason.encode!(%{error: "empty url"})
          else
            Jason.encode!(parse_url(url))
          end
        :gen_tcp.send(client, response <> "\n")
      {:error, _} ->
        :ok
    end
    :gen_tcp.close(client)
  end

  defp empty_to_nil(nil), do: nil
  defp empty_to_nil(""), do: nil
  defp empty_to_nil(val), do: val
end

URLParser.main(System.argv())
