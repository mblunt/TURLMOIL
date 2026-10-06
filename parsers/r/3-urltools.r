#!/usr/bin/env Rscript
# https://cran.r-project.org/web/packages/urltools/urltools.pdf

suppressMessages(library(urltools))
suppressMessages(library(jsonlite))

parse_url <- function(url) {
  tryCatch({
    parsed <- url_parse(url)  # returns a data frame with one row

    scheme    <- parsed$scheme[1]
    domain    <- parsed$domain[1]
    port      <- parsed$port[1]
    path      <- parsed$path[1]
    parameter <- parsed$parameter[1]  # raw query string
    fragment  <- parsed$fragment[1]


    list(
      scheme    = if (!is.null(scheme) && !is.na(scheme) && nchar(scheme) > 0) scheme else NULL,
      authority = "EXCLUDE",
      userinfo  = "EXCLUDE",
      username  = "EXCLUDE",
      password  = "EXCLUDE",
      host      = if (!is.null(domain) && !is.na(domain) && nchar(domain) > 0) domain else NULL,
      port      = if (!is.null(port) && !is.na(port) && nchar(port) > 0) as.character(port) else NULL,
      path      = if (!is.null(path) && !is.na(path) && nchar(path) > 0) path else NULL,
      query     = if (!is.null(parameter) && !is.na(parameter) && nchar(parameter) > 0) parameter else NULL,
      query_dict = "EXCLUDE",
      fragment  = if (!is.null(fragment) && !is.na(fragment) && nchar(fragment) > 0) fragment else NULL,
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
