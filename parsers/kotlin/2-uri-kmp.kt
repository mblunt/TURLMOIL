@file:JvmName("Parser")
// Kotlin URL parser using uri-kmp (com.eygraber:uri-kmp)
//
// Parses URLs using the eygraber/uri-kmp library — a Kotlin Multiplatform
// port of the AOSP (Android) Uri implementation. The AOSP parser is known
// to diverge from RFC 3986 in subtle ways, making it interesting for
// differential fuzzing against standard JVM parsers.

import com.eygraber.uri.Uri
import com.google.gson.GsonBuilder

private fun String?.orNull(): String? = if (isNullOrEmpty()) null else this

fun main(args: Array<String>) {
    val gson = GsonBuilder().serializeNulls().create()

    if (args.isEmpty()) {
        println(gson.toJson(mapOf("error" to "No URL provided")))
        return
    }

    val urlStr = args[0]
    val result = mutableMapOf<String, Any?>()

    try {
        val uri = Uri.parse(urlStr)

        result["scheme"] = uri.scheme.orNull()
        result["authority"] = "EXCLUDE"
        result["userinfo"] = uri.userInfo.orNull()
        result["username"] = "EXCLUDE"
        result["password"] = "EXCLUDE"
        result["host"] = uri.host.orNull()
        result["port"] = if (uri.port != -1) uri.port.toString() else null
        result["path"] = uri.path.orNull()
        result["query"] = uri.query.orNull()
        result["query_dict"] = "EXCLUDE"
        result["fragment"] = uri.fragment.orNull()
        result["raw_url"] = urlStr

    } catch (e: Exception) {
        result["error"] = e.message
        result["raw_url"] = urlStr
    }

    println(gson.toJson(result))
}
