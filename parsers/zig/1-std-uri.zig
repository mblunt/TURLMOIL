// std.Uri — Zig standard library RFC 3986 parser.
// Manually builds JSON to avoid std.json.stringify surprises across Zig versions.

const std = @import("std");

// Escape a string for JSON: wrap in quotes, escape special chars.
fn writeJsonString(w: anytype, s: []const u8) !void {
    try w.writeByte('"');
    for (s) |c| {
        switch (c) {
            '"' => try w.writeAll("\\\""),
            '\\' => try w.writeAll("\\\\"),
            '\n' => try w.writeAll("\\n"),
            '\r' => try w.writeAll("\\r"),
            '\t' => try w.writeAll("\\t"),
            0x08 => try w.writeAll("\\b"),
            0x0C => try w.writeAll("\\f"),
            else => try w.writeByte(c),
        }
    }
    try w.writeByte('"');
}

fn writeJsonOptString(w: anytype, key: []const u8, val: ?[]const u8, comma: bool) !void {
    if (comma) try w.writeByte(',');
    try w.writeByte('"');
    try w.writeAll(key);
    try w.writeAll("\":");
    if (val) |s| {
        try writeJsonString(w, s);
    } else {
        try w.writeAll("null");
    }
}

fn componentStr(c: std.Uri.Component) []const u8 {
    return switch (c) {
        .percent_encoded => |s| s,
        .raw => |s| s,
    };
}

fn optComponentStr(c: ?std.Uri.Component) ?[]const u8 {
    const comp = c orelse return null;
    const s = componentStr(comp);
    return if (s.len > 0) s else null;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const args = try std.process.argsAlloc(allocator);
    defer std.process.argsFree(allocator, args);

    const stdout = std.io.getStdOut().writer();

    if (args.len < 2) {
        try stdout.writeAll("{\"error\":\"No URL provided\"}\n");
        std.process.exit(1);
    }

    const url = args[1];

    const uri = std.Uri.parse(url) catch |err| {
        try stdout.writeAll("{\"error\":");
        try writeJsonString(stdout, @errorName(err));
        try stdout.writeAll(",\"raw_url\":");
        try writeJsonString(stdout, url);
        try stdout.writeAll("}\n");
        return;
    };

    var port_buf: [6]u8 = undefined;
    const port_str: ?[]const u8 = if (uri.port) |p|
        std.fmt.bufPrint(&port_buf, "{d}", .{p}) catch null
    else
        null;

    const scheme = if (uri.scheme.len > 0) @as(?[]const u8, uri.scheme) else null;
    const path_s = componentStr(uri.path);
    const path = if (path_s.len > 0) @as(?[]const u8, path_s) else null;

    var buf = std.ArrayList(u8).init(allocator);
    defer buf.deinit();
    const w = buf.writer();

    try w.writeByte('{');
    try writeJsonOptString(w, "scheme",     scheme,                    false);
    try writeJsonOptString(w, "authority",  "EXCLUDE",                 true);
    try writeJsonOptString(w, "userinfo",   "EXCLUDE",                 true);
    try writeJsonOptString(w, "username",   optComponentStr(uri.user),     true);
    try writeJsonOptString(w, "password",   optComponentStr(uri.password), true);
    try writeJsonOptString(w, "host",       optComponentStr(uri.host),     true);
    try writeJsonOptString(w, "port",       port_str,                  true);
    try writeJsonOptString(w, "path",       path,                      true);
    try writeJsonOptString(w, "query",      optComponentStr(uri.query),    true);
    try writeJsonOptString(w, "query_dict", "EXCLUDE",                 true);
    try writeJsonOptString(w, "fragment",   optComponentStr(uri.fragment), true);
    try writeJsonOptString(w, "raw_url",    url,                       true);
    try w.writeAll("}\n");

    try stdout.writeAll(buf.items);
}
