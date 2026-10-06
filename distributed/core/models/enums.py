import enum


class ParserLanguage(enum.Enum):
    ADA = "ada"
    BIN = "bin"
    CLOJURE = "clojure"
    CPP = "cpp"
    CRYSTAL = "crystal"
    CSHARP = "csharp"
    DART = "dart"
    ELIXIR = "elixir"
    ERLANG = "erlang"
    GO = "go"
    HASKELL = "haskell"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    KOTLIN = "kotlin"
    PERL = "perl"
    PHP = "php"
    PYTHON = "python"
    R = "r"
    RUBY = "ruby"
    RUST = "rust"
    SWIFT = "swift"
    ZIG = "zig"
    OTHER = "other"


class JobStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    PROCESSING = "processing"  # differential task is running
    PROCESSED = "processed"


class COMPARISON_FIELDS(enum.Enum):
    SCHEME = "scheme"
    AUTHORITY = "authority"
    USERINFO = "userinfo"
    USERNAME = "username"
    PASSWORD = "password"
    HOST = "host"
    PORT = "port"
    PATH = "path"
    QUERY = "query"
    QUERY_DICT = "query_dict"
    FRAGMENT = "fragment"
