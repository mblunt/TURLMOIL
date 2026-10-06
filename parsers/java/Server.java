import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class Server {

    interface Parser {
        Map<String, Object> parse(String url);
    }

    private static final Map<Integer, Parser> PARSERS = new HashMap<>();

    static {
        PARSERS.put(1, OkHttpParser::parseUrl);
        PARSERS.put(2, ApacheHttpClientParser::parseUrl);
        PARSERS.put(3, JavaNetURIParser::parseUrl);
        PARSERS.put(4, JavaNetURLParser::parseUrl);
        PARSERS.put(5, SpringWebParser::parseUrl);
        PARSERS.put(6, GalimatiasParser::parseUrl);
        PARSERS.put(7, NettyParser::parseUrl);
    }

    public static void main(String[] args) throws Exception {
        if (args.length < 2) {
            System.err.println("Usage: Server <port> <parser-number>");
            System.exit(1);
        }

        int port = Integer.parseInt(args[0]);
        int num = Integer.parseInt(args[1]);
        Parser parser = PARSERS.get(num);
        if (parser == null) {
            System.err.println("Unknown parser number: " + num);
            System.exit(1);
        }

        Gson gson = new GsonBuilder().serializeNulls().create();

        try (ServerSocket server = new ServerSocket(port)) {
            server.setReuseAddress(true);
            System.out.println("Java parser " + num + " ready on port " + port);
            System.out.flush();

            while (true) {
                Socket client = server.accept();
                new Thread(() -> {
                    try (
                        BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
                        PrintWriter out = new PrintWriter(client.getOutputStream(), true)
                    ) {
                        String url = in.readLine();
                        if (url == null || url.trim().isEmpty()) {
                            Map<String, Object> err = new HashMap<>();
                            err.put("error", "empty url");
                            out.println(gson.toJson(err));
                            return;
                        }
                        Map<String, Object> result = parser.parse(url.trim());
                        out.println(gson.toJson(result));
                    } catch (Exception ignored) {
                    } finally {
                        try { client.close(); } catch (Exception ignored) {}
                    }
                }).start();
            }
        }
    }
}
