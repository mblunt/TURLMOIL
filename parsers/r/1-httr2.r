#!/usr/bin/env Rscript
# https://httr2.r-lib.org/reference/url_parse.html

suppressMessages(library(httr2))
suppressMessages(library(jsonlite))

parse_url <- function(url) {
  tryCatch({
    parsed <- url_parse(url)

    list(
      scheme    = if (!is.null(parsed$scheme) && nchar(parsed$scheme) > 0) parsed$scheme else NULL,
      authority = "EXCLUDE",
      userinfo  = "EXCLUDE",
      username  = if (!is.null(parsed$username) && !is.na(parsed$username) && nchar(parsed$username) > 0) parsed$username else NULL,
      password  = if (!is.null(parsed$password) && !is.na(parsed$password) && nchar(parsed$password) > 0) parsed$password else NULL,
      host      = if (!is.null(parsed$hostname) && nchar(parsed$hostname) > 0) parsed$hostname else NULL,
      port      = if (!is.null(parsed$port) && !is.na(parsed$port)) as.character(parsed$port) else NULL,
      path      = if (!is.null(parsed$path) && nchar(parsed$path) > 0) parsed$path else NULL,
      query     = "EXCLUDE",
      query_dict = if (!is.null(parsed$query) && length(parsed$query) > 0) parsed$query else NULL,
      fragment  = if (!is.null(parsed$fragment) && !is.na(parsed$fragment) && nchar(parsed$fragment) > 0) parsed$fragment else NULL,
      raw_url   = url
    )
  }, error = function(e) {
    list(error = conditionMessage(e), raw_url = url)
  })
}

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) {
  cat(toJSON(list(error = "No URL provided"), auto_unbox = TRUE), "\n")
  quit(status = 1)
}

result <- parse_url(args[1])
cat(toJSON(result, auto_unbox = TRUE, null = "null"), "\n")
