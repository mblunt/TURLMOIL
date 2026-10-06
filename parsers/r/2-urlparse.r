#!/usr/bin/env Rscript
# https://cran.r-project.org/web/packages/urlparse/refman/urlparse.html#url_parse

suppressMessages(library(urlparse))
suppressMessages(library(jsonlite))

parse_url <- function(url) {
  tryCatch({
    parsed <- url_parse(url)

    list(
      scheme    = if (!is.null(parsed$scheme) && !is.na(parsed$scheme) && nchar(parsed$scheme) > 0) parsed$scheme else NULL,
      authority = "EXCLUDE",
      userinfo  = "EXCLUDE",
      username  = if (!is.null(parsed$user) && !is.na(parsed$user) && nchar(parsed$user) > 0) parsed$user else NULL,
      password  = if (!is.null(parsed$password) && !is.na(parsed$password) && nchar(parsed$password) > 0) parsed$password else NULL,
      host      = if (!is.null(parsed$host) && !is.na(parsed$host) && nchar(parsed$host) > 0) parsed$host else NULL,
      port      = if (!is.null(parsed$port) && !is.na(parsed$port) && nchar(parsed$port) > 0) as.character(parsed$port) else NULL,
      path      = if (!is.null(parsed$path) && !is.na(parsed$path) && nchar(parsed$path) > 0) parsed$path else NULL,
      query     = if (!is.null(parsed$raw_query) && !is.na(parsed$raw_query) && nchar(parsed$raw_query) > 0) parsed$raw_query else NULL,
      query_dict = "EXCLUDE",
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
