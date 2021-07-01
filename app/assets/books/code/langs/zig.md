# Zig

https://ziglang.org/

general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software

```c++
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Hello, {}!\n", .{"world"});
}
>$ zig build-exe hello.zig
$ ./hello
Hello, world!

```

```c++
const std = @import("std");
const json = std.json;
const payload =
    \\{
    \\    "vals": {
    \\        "testing": 1,
    \\        "production": 42
    \\    },
    \\    "uptime": 9999
    \\}
;
const Config = struct {
    vals: struct { testing: u8, production: u8 },
    uptime: u64,
};
const config = x: {
    var stream = json.TokenStream.init(payload);
    const res = json.parse(Config, &stream, .{});
    // Assert no error can occur since we are
    // parsing this JSON at comptime!
    break :x res catch unreachable;
};
pub fn main() !void {
    if (config.vals.production > 50) {
        @compileError("only up to 50 supported");
    }
    std.log.info("up={d}", .{config.uptime});
}
```