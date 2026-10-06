require "uri"
require "json"

# Re-open the standard library struct to bypass the 'protected' lock
struct URI::Params
  def to_h_arrays
    @raw_params
  end
end

struct URLResult
  include JSON::Serializable

  def initialize; end

  @[JSON::Field(emit_null: false)]
  property path : String?

  @[JSON::Field(emit_null: false)]
  property userinfo : String?

  @[JSON::Field(emit_null: false)]
  property fragment : String?

  @[JSON::Field(emit_null: false)]
  property query_dict : Hash(String, Array(String))?

  @[JSON::Field(emit_null: false)]
  property username : String?

  @[JSON::Field(emit_null: false)]
  property scheme : String?

  @[JSON::Field(emit_null: false)]
  property password : String?

  @[JSON::Field(emit_null: false)]
  property authority : String?

  @[JSON::Field(emit_null: false)]
  property host : String?

  @[JSON::Field(emit_null: false)]
  property query : String?

  @[JSON::Field(emit_null: false)]
  property raw_url : String?

  @[JSON::Field(emit_null: false)]
  property error : String?
end

if ARGV.empty?
  STDERR.puts "Error: No URL provided."
  exit 1
end

raw_url = ARGV[0]

begin
  uri = URI.parse(raw_url)
  result = URLResult.new

  result.scheme = uri.scheme
  result.userinfo = "EXCLUDE"
  result.username = uri.user
  result.password = uri.password
  result.authority = uri.authority
  result.host = uri.host
  
  # Exclude path if it's completely empty
  result.path = uri.path.to_s.empty? ? nil : uri.path
  
  result.query = uri.query
  
  params = uri.query_params
  # Grab the pre-built dictionary directly from the standard library
  dict = uri.query_params.to_h_arrays
  
  result.query_dict = dict.empty? ? nil : dict
  
  result.fragment = uri.fragment
  result.raw_url = raw_url

  puts result.to_json
rescue ex
  error_result = URLResult.new
  error_result.raw_url = raw_url
  error_result.error = "Failed to parse URL: #{ex.message}"
  puts error_result.to_json
end
