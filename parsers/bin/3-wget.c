/*
 * Build with:
 *   gcc -O2 3-wget.c $(pkg-config --cflags --libs libwget) -o 3-wget
 */

#include <stdio.h>
#include <string.h>
#include <stdint.h>

#include <wget.h>

/* Print a JSON-encoded string value including surrounding quotes.
 * Handles all JSON special characters; null pointer prints JSON null. */
static void print_json_string(const char *value)
{
	if (!value) {
		fputs("null", stdout);
		return;
	}

	putchar('"');
	for (const unsigned char *p = (const unsigned char *)value; *p; p++) {
		switch (*p) {
		case '"':  fputs("\\\"", stdout); break;
		case '\\': fputs("\\\\", stdout); break;
		case '\n': fputs("\\n",  stdout); break;
		case '\r': fputs("\\r",  stdout); break;
		case '\t': fputs("\\t",  stdout); break;
		case '\b': fputs("\\b",  stdout); break;
		case '\f': fputs("\\f",  stdout); break;
		default:
			if (*p < 0x20)
				printf("\\u%04x", (unsigned)*p);
			else
				putchar(*p);
		}
	}
	putchar('"');
}

int main(int argc, char **argv)
{
	if (argc != 2) {
		fprintf(stdout, "{\"error\":\"No URL provided\"}\n");
		return 1;
	}

	wget_iri *iri = wget_iri_parse(argv[1], NULL);

	if (!iri) {
		fputs("{\"error\":\"failed to parse URL\",\"raw_url\":", stdout);
		print_json_string(argv[1]);
		fputs("}\n", stdout);
		return 1;
	}

	char port_buf[8] = "";
	if (iri->port_given)
		snprintf(port_buf, sizeof(port_buf), "%u", (unsigned)iri->port);

	fputs("{", stdout);
	fputs("\"scheme\":",     stdout); print_json_string(wget_iri_scheme_get_name(iri->scheme));
	fputs(",\"authority\":\"EXCLUDE\"", stdout);
	fputs(",\"userinfo\":",  stdout); print_json_string(iri->userinfo);
	fputs(",\"username\":\"EXCLUDE\"", stdout);
	fputs(",\"password\":",  stdout); print_json_string(iri->password);
	fputs(",\"host\":",      stdout); print_json_string(iri->host);
	fputs(",\"port\":",      stdout); print_json_string(port_buf[0] ? port_buf : NULL);
	fputs(",\"path\":",      stdout); print_json_string(iri->path);
	fputs(",\"query\":",     stdout); print_json_string(iri->query);
	fputs(",\"query_dict\":\"EXCLUDE\"", stdout);
	fputs(",\"fragment\":",  stdout); print_json_string(iri->fragment);
	fputs(",\"raw_url\":",   stdout); print_json_string(argv[1]);
	fputs("}\n", stdout);

	wget_iri_free(&iri);

	return 0;
}
