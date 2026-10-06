#!/bin/sh

# Build Zig parsers in /parsers/zig into /parsers/zig/<stem>.
# Supports both stdlib-only single-file builds and projects that need
# `zig fetch` + a generated build.zig.

set -u

failed=0

commands=$(jq -r '.parsers[] | select(.language == "zig") | .command' /parsers/parsers.json)

while IFS= read -r cmd; do
    stem=$(basename "$cmd")
    f="/parsers/zig/$stem.zig"
    lib_suffix=$(echo "$stem" | cut -d'-' -f2-)
    id_key="zig-$lib_suffix"

    dep_url=$(sh /parsers/extractor.sh "$id_key" dep_url)
    dep_name=$(sh /parsers/extractor.sh "$id_key" dep_name)
    dep_module=$(sh /parsers/extractor.sh "$id_key" dep_module)
    if [ "$dep_name" = "null" ] || [ -z "$dep_name" ]; then
        dep_name="$dep_module"
    fi

    echo "=== Building $id_key ==="

    if [ "$dep_url" = "null" ] || [ -z "$dep_url" ]; then
        if ! zig build-exe -O ReleaseSafe -femit-bin="/parsers/zig/$stem" "$f"; then
            failed=1
        else
            chmod +x "/parsers/zig/$stem" 2>/dev/null || true
        fi
        continue
    fi

    rm -rf "/build/$id_key"
    mkdir -p "/build/$id_key"
    cd "/build/$id_key" || exit 1

    # Generate Zig 0.14 project scaffold (includes required fingerprint)
    if ! zig init >/dev/null; then
        failed=1
        cd /build || exit 1
        continue
    fi

    cp "$f" "src/main.zig"

    # Overwrite build.zig to reference the fetched dep
    printf 'const std = @import("std");\npub fn build(b: *std.Build) void {\n    const target = b.standardTargetOptions(.{});\n    const optimize = b.standardOptimizeOption(.{});\n    const dep = b.dependency("%s", .{ .target = target, .optimize = optimize });\n    const exe = b.addExecutable(.{\n        .name = "%s",\n        .root_source_file = b.path("src/main.zig"),\n        .target = target,\n        .optimize = optimize,\n    });\n    exe.root_module.addImport("%s", dep.module("%s"));\n    b.installArtifact(exe);\n}\n' \
        "$dep_name" "$id_key" "$dep_module" "$dep_module" > build.zig

    if ! zig fetch --save="$dep_name" "$dep_url"; then
        failed=1
        cd /build || exit 1
        continue
    fi

    if ! zig build -Doptimize=ReleaseSafe; then
        failed=1
        cd /build || exit 1
        continue
    fi

    if ! cp "zig-out/bin/$id_key" "/parsers/zig/$stem"; then
        failed=1
        cd /build || exit 1
        continue
    fi

    chmod +x "/parsers/zig/$stem" 2>/dev/null || true

    cd /build || exit 1
done <<EOF
$commands
EOF

exit "$failed"
