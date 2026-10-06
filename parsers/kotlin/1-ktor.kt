@file:JvmName("Parser")
// Kotlin URL parser using Ktor HTTP (io.ktor:ktor-http)
//
// Parses URLs using Ktor's Url class and outputs JSON.
// Ktor has its own URL parsing implementation (not a simple java.net.URI wrapper)
// with custom handling for encoded components and multiplatform support.

import io.ktor.http.Url
import com.google.gson.GsonBuilder

// Avoids type-inference ambiguity when assigning to MutableMap<String, Any?>
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
        val url = Url(urlStr)

        result["scheme"] = url.protocol.name.orNull()
        result["authority"] = "EXCLUDE"
        result["userinfo"] = "EXCLUDE"
        result["username"] = url.user.orNull()
        result["password"] = url.password.orNull()
        result["host"] = url.host.orNull()
        val effectivePort = url.port
        val defaultPort = url.protocol.defaultPort
        result["port"] = if (effectivePort != defaultPort) effectivePort.toString() else null
        result["path"] = url.encodedPath.orNull()
        result["query"] = url.encodedQuery.orNull()
        result["query_dict"] = "EXCLUDE"
        result["fragment"] = url.encodedFragment.orNull()
        result["raw_url"] = urlStr

    } catch (e: Exception) {
        result["error"] = e.message
        result["raw_url"] = urlStr
    }

    println(gson.toJson(result))
}
