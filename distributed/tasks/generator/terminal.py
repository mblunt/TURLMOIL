import string

# List of all known URI schemes as per IANA and common usage.
# Source: https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml
KNOWN_SCHEMES = [
    "aaa", "aaas", "about", "acap", "acct", "acr", "adiumxtra", "afp", "afs", "aim", "appdata",
    "apt", "attachment", "aw", "barion", "beshare", "bitcoin", "blob", "bolo", "browserext",
    "callto", "cap", "chrome", "chrome-extension", "cid", "coap", "coaps", "com-eventbrite-attendee",
    "content", "crid", "cvs", "data", "dav", "dict", "did", "dis", "dlna-playsingle", "dlna-playcontainer",
    "dns", "dntp", "doi", "dpp", "drm", "drop", "dtmi", "dtn", "dvb", "ed2k", "elsi", "example",
    "facetime", "fax", "feed", "feedready", "file", "filesystem", "finger", "first-run-pen-experience",
    "fish", "fm", "ftp", "geo", "gg", "git", "gizmoproject", "go", "gopher", "graph", "gtalk",
    "h323", "ham", "hcp", "http", "https", "hxxp", "hxxps", "hydrazone", "iax", "icap", "icon",
    "im", "imap", "info", "iotdisco", "ipn", "ipp", "ipps", "irc", "irc6", "ircs", "iris", "iris.beep",
    "iris.xpc", "iris.xpcs", "iris.lwz", "itms", "jabber", "jar", "jms", "keyparc", "lastfm",
    "ldap", "ldaps", "lvlt", "magnet", "mailserver", "mailto", "maps", "market", "message", "mid",
    "mms", "modem", "mongodb", "moz", "ms-access", "ms-browser-extension", "ms-drive-to", "ms-enrollment",
    "ms-excel", "ms-gamebarservices", "ms-getoffice", "ms-help", "ms-infopath", "ms-media-stream-id",
    "ms-project", "ms-powerpoint", "ms-publisher", "ms-search", "ms-secondary-screen-controller",
    "ms-secondary-screen-setup", "ms-settings", "ms-settings-airplanemode", "ms-settings-bluetooth",
    "ms-settings-camera", "ms-settings-cellular", "ms-settings-cloudstorage", "ms-settings-connectabledevices",
    "ms-settings-displays-topology", "ms-settings-emailandaccounts", "ms-settings-language",
    "ms-settings-location", "ms-settings-lock", "ms-settings-nfctransactions", "ms-settings-notifications",
    "ms-settings-power", "ms-settings-privacy", "ms-settings-proximity", "ms-settings-screenrotation",
    "ms-settings-wifi", "ms-settings-workplace", "ms-spd", "ms-sttoverlay", "ms-transit-to",
    "ms-useractivityset", "ms-virtualtouchpad", "ms-visio", "ms-walk-to", "ms-whiteboard", "ms-whiteboard-cmd",
    "ms-word", "msnim", "msrp", "msrps", "mtqp", "mumble", "mupdate", "mvn", "news", "nfs", "ni",
    "nih", "nntp", "notes", "ocf", "oid", "onenote", "onenote-cmd", "opaquelocktoken", "openpgp4fpr",
    "otpauth", "palm", "paparazzi", "pkcs11", "platform", "pop", "pres", "prospero", "proxy",
    "pwid", "psyc", "pttp", "qb", "query", "redis", "rediss", "reload", "res", "resource", "rmi",
    "rsync", "rtmfp", "rtmp", "rtsp", "rtsps", "rtspu", "secondlife", "service", "session", "sftp",
    "sgn", "shttp", "sieve", "sip", "sips", "skype", "smb", "sms", "smtp", "snews", "snmp", "soap.beep",
    "soap.beeps", "soldat", "spotify", "ssh", "steam", "stun", "stuns", "submit", "svn", "tag",
    "teamspeak", "tel", "teliaeid", "telnet", "tftp", "things", "thismessage", "tn3270", "tip",
    "tns", "tool", "turn", "turns", "tv", "udp", "unreal", "urn", "ut2004", "v-event", "vemmi",
    "ventrilo", "videotex", "vnc", "view-source", "wais", "webcal", "wpid", "ws", "wss", "wtai",
    "wyciwyg", "xcon", "xcon-userid", "xfire", "xmlrpc.beep", "xmlrpc.beeps", "xmpp", "xri", "ymsgr",
    "z39.50r", "z39.50s"
]

COMMON_SCHEMES = [
    "http", "https", "ftp", "file", "data", "ws", "wss"
]

HOST_SPECIAL = ["-", "."]
PATH_SPECIAL = ["!", "@", "$", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", "\"", "'", ",", ".", "/", "\\", "|", "~", "`"]
PATH_FORBIDDEN = ["?", "#"]
QUERY_SPECIAL = ["!", "@", "$", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", ":", ";", "\"", "'", ",", ".", "/", "\\", "|", "~", "`"]

NULL = [""]

ASCII_DIGITS = string.digits
ASCII_LETTERS = string.ascii_letters
ASCII_WHITESPACE = string.whitespace
ASCII_SPECIAL = string.punctuation
ASCII_CONTROL = "".join(chr(i) for i in range(0x00, 0x20)) + chr(0x7F)
HEXDIGIT = string.hexdigits
# UNICODE_VALID
# UNICODE_DISALLOWED
# UNICODE_UNASSIGNED
# UNICODE_RESERVED


# ---------------------------------------------------------------------------
# Shared range-expansion helper (used by all Unicode sets below)
# ---------------------------------------------------------------------------

def _expand_iana_ranges(ranges: list[str]) -> str:
    """
    Expand hex range strings (e.g. "0041-005A", "007F") into a string of
    the corresponding Unicode characters.
    Surrogates (U+D800-U+DFFF) are skipped — Python str cannot represent them.
    """
    chars: list[str] = []
    for entry in ranges:
        if "-" in entry:
            lo_s, hi_s = entry.split("-", 1)
            lo, hi = int(lo_s, 16), int(hi_s, 16)
        else:
            lo = hi = int(entry, 16)
        for cp in range(lo, hi + 1):
            if 0xD800 <= cp <= 0xDFFF:
                continue
            if cp > 0x10FFFF:
                break
            chars.append(chr(cp))
    return "".join(chars)


# ---------------------------------------------------------------------------
# UNICODE_VALID — PVALID + CONTEXTJ + CONTEXTO from IANA IDNA 6.3.0
# CONTEXTJ and CONTEXTO are join/other context-rule characters that are
# valid in labels when their context rules are satisfied; treated as Valid
# for fuzzing purposes.
# Source: https://www.iana.org/assignments/idna-tables-6.3.0/idna-tables-6.3.0.xhtml
# ---------------------------------------------------------------------------

_IANA_PVALID_RANGES: list[str] = [
    "002D", "0030-0039", "0061-007A", "00DF-00F6", "00F8-00FF",
    "0101", "0103", "0105", "0107", "0109", "010B", "010D", "010F",
    "0111", "0113", "0115", "0117", "0119", "011B", "011D", "011F",
    "0121", "0123", "0125", "0127", "0129", "012B", "012D", "012F",
    "0131", "0135", "0137-0138", "013A", "013C", "013E", "0142",
    "0144", "0146", "0148", "014B", "014D", "014F", "0151", "0153",
    "0155", "0157", "0159", "015B", "015D", "015F", "0161", "0163",
    "0165", "0167", "0169", "016B", "016D", "016F", "0171", "0173",
    "0175", "0177", "017A", "017C", "017E", "0180", "0183", "0185",
    "0188", "018C-018D", "0192", "0195", "0199-019B", "019E", "01A1",
    "01A3", "01A5", "01A8", "01AA-01AB", "01AD", "01B0", "01B4",
    "01B6", "01B9-01BB", "01BD-01C3", "01CE", "01D0", "01D2", "01D4",
    "01D6", "01D8", "01DA", "01DC-01DD", "01DF", "01E1", "01E3",
    "01E5", "01E7", "01E9", "01EB", "01ED", "01EF-01F0", "01F5",
    "01F9", "01FB", "01FD", "01FF",
    "0201", "0203", "0205", "0207", "0209", "020B", "020D", "020F",
    "0211", "0213", "0215", "0217", "0219", "021B", "021D", "021F",
    "0221", "0223", "0225", "0227", "0229", "022B", "022D", "022F",
    "0231", "0233-0239", "023C", "023F-0240", "0242", "0247", "0249",
    "024B", "024D", "024F-02AF", "02B9-02C1", "02C6-02D1", "02EC",
    "02EE", "0300-033F", "0342", "0346-034E", "0350-036F", "0371",
    "0373", "0377", "037B-037D", "0390", "03AC-03CE", "03D7", "03D9",
    "03DB", "03DD", "03DF", "03E1", "03E3", "03E5", "03E7", "03E9",
    "03EB", "03ED", "03EF", "03F3", "03F8", "03FB-03FC",
    "0430-045F", "0461", "0463", "0465", "0467", "0469", "046B",
    "046D", "046F", "0471", "0473", "0475", "0477", "0479", "047B",
    "047D", "047F", "0481", "0483-0487", "048B", "048D", "048F",
    "0491", "0493", "0495", "0497", "0499", "049B", "049D", "049F",
    "04A1", "04A3", "04A5", "04A7", "04A9", "04AB", "04AD", "04AF",
    "04B1", "04B3", "04B5", "04B7", "04B9", "04BB", "04BD", "04BF",
    "04C2", "04C4", "04C6", "04C8", "04CA", "04CC", "04CE-04CF",
    "04D1", "04D3", "04D5", "04D7", "04D9", "04DB", "04DD", "04DF",
    "04E1", "04E3", "04E5", "04E7", "04E9", "04EB", "04ED", "04EF",
    "04F1", "04F3", "04F5", "04F7", "04F9", "04FB", "04FD", "04FF",
    "0501", "0503", "0505", "0507", "0509", "050B", "050D", "050F",
    "0511", "0513", "0515", "0517", "0519", "051B", "051D", "051F",
    "0521", "0523", "0525", "0527", "0559", "0561-0586",
    "0591-05BD", "05BF", "05C1-05C2", "05C4-05C5", "05C7",
    "05D0-05EA", "05F0-05F2",
    "0610-061A", "0620-063F", "0641-065F", "066E-0674", "0679-06D3",
    "06D5-06DC", "06DF-06E8", "06EA-06EF", "06FA-06FF",
    "0710-074A", "074D-07B1", "07C0-07F5",
    "0800-082D", "0840-085B", "08A0", "08A2-08AC", "08E4-08FE",
    "0900-0957", "0960-0963", "0966-096F", "0971-0977", "0979-097F",
    "0981-0983", "0985-098C", "098F-0990", "0993-09A8", "09AA-09B0",
    "09B2", "09B6-09B9", "09BC-09C4", "09C7-09C8", "09CB-09CE",
    "09D7", "09E0-09E3", "09E6-09F1",
    "0A01-0A03", "0A05-0A0A", "0A0F-0A10", "0A13-0A28", "0A2A-0A30",
    "0A32", "0A35", "0A38-0A39", "0A3C", "0A3E-0A42", "0A47-0A48",
    "0A4B-0A4D", "0A51", "0A5C", "0A66-0A75",
    "0A81-0A83", "0A85-0A8D", "0A8F-0A91", "0A93-0AA8", "0AAA-0AB0",
    "0AB2-0AB3", "0AB5-0AB9", "0ABC-0AC5", "0AC7-0AC9", "0ACB-0ACD",
    "0AD0", "0AE0-0AE3", "0AE6-0AEF",
    "0B01-0B03", "0B05-0B0C", "0B0F-0B10", "0B13-0B28", "0B2A-0B30",
    "0B32-0B33", "0B35-0B39", "0B3C-0B44", "0B47-0B48", "0B4B-0B4D",
    "0B56-0B57", "0B5F-0B63", "0B66-0B6F", "0B71",
    "0B82-0B83", "0B85-0B8A", "0B8E-0B90", "0B92-0B95", "0B99-0B9A",
    "0B9C", "0B9E-0B9F", "0BA3-0BA4", "0BA8-0BAA", "0BAE-0BB9",
    "0BBE-0BC2", "0BC6-0BC8", "0BCA-0BCD", "0BD0", "0BD7",
    "0BE6-0BEF",
    "0C01-0C03", "0C05-0C0C", "0C0E-0C10", "0C12-0C28", "0C2A-0C33",
    "0C35-0C39", "0C3D-0C44", "0C46-0C48", "0C4A-0C4D", "0C55-0C56",
    "0C58-0C59", "0C60-0C63", "0C66-0C6F",
    "0C82-0C83", "0C85-0C8C", "0C8E-0C90", "0C92-0CA8", "0CAA-0CB3",
    "0CB5-0CB9", "0CBC-0CC4", "0CC6-0CC8", "0CCA-0CCD", "0CD5-0CD6",
    "0CDE", "0CE0-0CE3", "0CE6-0CEF", "0CF1-0CF2",
    "0D02-0D03", "0D05-0D0C", "0D0E-0D10", "0D12-0D3A", "0D3D-0D44",
    "0D46-0D48", "0D4A-0D4E", "0D57", "0D60-0D63", "0D66-0D6F",
    "0D7A-0D7F",
    "0D82-0D83", "0D85-0D96", "0D9A-0DB1", "0DB3-0DBB", "0DBD",
    "0DC0-0DC6", "0DCA", "0DCF-0DD4", "0DD6", "0DD8-0DDF",
    "0DF2-0DF3",
    "0E01-0E32", "0E34-0E3A", "0E40-0E4E", "0E50-0E59",
    "0E81-0E82", "0E84", "0E87-0E88", "0E8A", "0E8D", "0E94-0E97",
    "0E99-0E9F", "0EA1-0EA3", "0EA5", "0EA7", "0EAA-0EAB",
    "0EAD-0EB2", "0EB4-0EB9", "0EBB-0EBD", "0EC0-0EC4", "0EC6",
    "0EC8-0ECD", "0ED0-0ED9", "0EDE-0EDF",
    "0F00", "0F0B", "0F18-0F19", "0F20-0F29", "0F35", "0F37", "0F39",
    "0F3E-0F42", "0F44-0F47", "0F49-0F4C", "0F4E-0F51", "0F53-0F56",
    "0F58-0F5B", "0F5D-0F68", "0F6A-0F6C", "0F71-0F72", "0F74",
    "0F7A-0F80", "0F82-0F84", "0F86-0F92", "0F94-0F97", "0F99-0F9C",
    "0F9E-0FA1", "0FA3-0FA6", "0FA8-0FAB", "0FAD-0FB8", "0FBA-0FBC",
    "0FC6",
    "1000-1049", "1050-109D", "10D0-10FA", "10FD-10FF",
    "1200-1248", "124A-124D", "1250-1256", "1258", "125A-125D",
    "1260-1288", "128A-128D", "1290-12B0", "12B2-12B5", "12B8-12BE",
    "12C0", "12C2-12C5", "12C8-12D6", "12D8-1310", "1312-1315",
    "1318-135A", "135D-135F", "1380-138F", "13A0-13F4",
    "1401-166C", "166F-167F", "1681-169A", "16A0-16EA",
    "1700-170C", "170E-1714", "1720-1734", "1740-1753", "1760-176C",
    "176E-1770", "1772-1773",
    "1780-17B3", "17B6-17D3", "17D7", "17DC-17DD", "17E0-17E9",
    "1810-1819", "1820-1877", "1880-18AA", "18B0-18F5",
    "1900-191C", "1920-192B", "1930-193B", "1946-196D", "1970-1974",
    "1980-19AB", "19B0-19C9", "19D0-19D9",
    "1A00-1A1B", "1A20-1A5E", "1A60-1A7C", "1A7F-1A89", "1A90-1A99",
    "1AA7",
    "1B00-1B4B", "1B50-1B59", "1B6B-1B73", "1B80-1BF3",
    "1C00-1C37", "1C40-1C49", "1C4D-1C7D", "1CD0-1CD2", "1CD4-1CF6",
    "1D00-1D2B", "1D2F", "1D3B", "1D4E", "1D6B-1D77", "1D79-1D9A",
    "1DC0-1DE6", "1DFC-1DFF",
    "1E01", "1E03", "1E05", "1E07", "1E09", "1E0B", "1E0D", "1E0F",
    "1E11", "1E13", "1E15", "1E17", "1E19", "1E1B", "1E1D", "1E1F",
    "1E21", "1E23", "1E25", "1E27", "1E29", "1E2B", "1E2D", "1E2F",
    "1E31", "1E33", "1E35", "1E37", "1E39", "1E3B", "1E3D", "1E3F",
    "1E41", "1E43", "1E45", "1E47", "1E49", "1E4B", "1E4D", "1E4F",
    "1E51", "1E53", "1E55", "1E57", "1E59", "1E5B", "1E5D", "1E5F",
    "1E61", "1E63", "1E65", "1E67", "1E69", "1E6B", "1E6D", "1E6F",
    "1E71", "1E73", "1E75", "1E77", "1E79", "1E7B", "1E7D", "1E7F",
    "1E81", "1E83", "1E85", "1E87", "1E89", "1E8B", "1E8D", "1E8F",
    "1E91", "1E93", "1E95-1E99", "1E9C-1E9D", "1E9F",
    "1EA1", "1EA3", "1EA5", "1EA7", "1EA9", "1EAB", "1EAD", "1EAF",
    "1EB1", "1EB3", "1EB5", "1EB7", "1EB9", "1EBB", "1EBD", "1EBF",
    "1EC1", "1EC3", "1EC5", "1EC7", "1EC9", "1ECB", "1ECD", "1ECF",
    "1ED1", "1ED3", "1ED5", "1ED7", "1ED9", "1EDB", "1EDD", "1EDF",
    "1EE1", "1EE3", "1EE5", "1EE7", "1EE9", "1EEB", "1EED", "1EEF",
    "1EF1", "1EF3", "1EF5", "1EF7", "1EF9", "1EFB", "1EFD",
    "1EFF-1F07", "1F10-1F15", "1F20-1F27", "1F30-1F37", "1F40-1F45",
    "1F50-1F57", "1F60-1F67", "1F70", "1F72", "1F74", "1F76", "1F78",
    "1F7A", "1F7C", "1FB0-1FB1", "1FB6", "1FC6", "1FD0-1FD2",
    "1FD6-1FD7", "1FE0-1FE2", "1FE4-1FE7", "1FF6",
    "214E", "2184",
    "2C30-2C5E", "2C61", "2C65-2C66", "2C68", "2C6A", "2C6C", "2C71",
    "2C73-2C74", "2C76-2C7B",
    "2C81", "2C83", "2C85", "2C87", "2C89", "2C8B", "2C8D", "2C8F",
    "2C91", "2C93", "2C95", "2C97", "2C99", "2C9B", "2C9D", "2C9F",
    "2CA1", "2CA3", "2CA5", "2CA7", "2CA9", "2CAB", "2CAD", "2CAF",
    "2CB1", "2CB3", "2CB5", "2CB7", "2CB9", "2CBB", "2CBD", "2CBF",
    "2CC1", "2CC3", "2CC5", "2CC7", "2CC9", "2CCB", "2CCD", "2CCF",
    "2CD1", "2CD3", "2CD5", "2CD7", "2CD9", "2CDB", "2CDD", "2CDF",
    "2CE1", "2CE3-2CE4", "2CEC", "2CEE-2CF1", "2CF3",
    "2D00-2D25", "2D27", "2D2D", "2D30-2D67", "2D7F-2D96",
    "2DA0-2DA6", "2DA8-2DAE", "2DB0-2DB6", "2DB8-2DBE", "2DC0-2DC6",
    "2DC8-2DCE", "2DD0-2DD6", "2DD8-2DDE", "2DE0-2DFF", "2E2F",
    "3005-3007", "302A-302D", "303C", "3041-3096", "3099-309A",
    "309D-309E", "30A1-30FA", "30FC-30FE", "3105-312D", "31A0-31BA",
    "31F0-31FF", "3400-4DB5", "4E00-9FCC",
    "A000-A48C", "A4D0-A4FD", "A500-A60C", "A610-A62B",
    "A641", "A643", "A645", "A647", "A649", "A64B", "A64D", "A64F",
    "A651", "A653", "A655", "A657", "A659", "A65B", "A65D", "A65F",
    "A661", "A663", "A665", "A667", "A669", "A66B", "A66D-A66F",
    "A674-A67D", "A67F",
    "A681", "A683", "A685", "A687", "A689", "A68B", "A68D", "A68F",
    "A691", "A693", "A695", "A697", "A69F-A6E5", "A6F0-A6F1",
    "A717-A71F",
    "A723", "A725", "A727", "A729", "A72B", "A72D", "A72F-A731",
    "A733", "A735", "A737", "A739", "A73B", "A73D", "A73F",
    "A741", "A743", "A745", "A747", "A749", "A74B", "A74D", "A74F",
    "A751", "A753", "A755", "A757", "A759", "A75B", "A75D", "A75F",
    "A761", "A763", "A765", "A767", "A769", "A76B", "A76D", "A76F",
    "A771-A778", "A77A", "A77C", "A77F",
    "A781", "A783", "A785", "A787-A788", "A78C", "A78E", "A791",
    "A793", "A7A1", "A7A3", "A7A5", "A7A7", "A7A9", "A7FA-A827",
    "A840-A873", "A880-A8C4", "A8D0-A8D9", "A8E0-A8F7", "A8FB",
    "A900-A92D", "A930-A953", "A980-A9C0", "A9CF-A9D9",
    "AA00-AA36", "AA40-AA4D", "AA50-AA59", "AA60-AA76", "AA7A-AA7B",
    "AA80-AAC2", "AADB-AADD", "AAE0-AAEF", "AAF2-AAF6",
    "AB01-AB06", "AB09-AB0E", "AB11-AB16", "AB20-AB26", "AB28-AB2E",
    "ABC0-ABEA", "ABEC-ABED", "ABF0-ABF9",
    "AC00-D7A3",
    "FA0E-FA0F", "FA11", "FA13-FA14", "FA1F", "FA21", "FA23-FA24",
    "FA27-FA29", "FB1E", "FE20-FE26", "FE73",
    "10000-1000B", "1000D-10026", "10028-1003A", "1003C-1003D",
    "1003F-1004D", "10050-1005D", "10080-100FA", "101FD",
    "10280-1029C", "102A0-102D0",
    "10300-1031E", "10330-10340", "10342-10349", "10380-1039D",
    "103A0-103C3", "103C8-103CF", "10428-1049D", "104A0-104A9",
    "10800-10805", "10808", "1080A-10835", "10837-10838", "1083C",
    "1083F-10855", "10900-10915", "10920-10939",
    "10980-109B7", "109BE-109BF",
    "10A00-10A03", "10A05-10A06", "10A0C-10A13", "10A15-10A17",
    "10A19-10A33", "10A38-10A3A", "10A3F", "10A60-10A7C",
    "10B00-10B35", "10B40-10B55", "10B60-10B72", "10C00-10C48",
    "11000-11046", "11066-1106F", "11080-110BA", "110D0-110E8",
    "110F0-110F9", "11100-11134", "11136-1113F", "11180-111C4",
    "111D0-111D9", "11680-116B7", "116C0-116C9",
    "12000-1236E", "13000-1342E",
    "16800-16A38", "16F00-16F44", "16F50-16F7E", "16F8F-16F9F",
    "1B000-1B001",
    "20000-2A6D6", "2A700-2B734", "2B740-2B81D",
]

# CONTEXTJ: Zero Width Non-Joiner (U+200C) and Zero Width Joiner (U+200D).
# CONTEXTO: Middle Dot, Greek Lower Numeral Sign, Hebrew Punctuation Geresh
#           & Gershayim, Arabic-Indic Digits, Extended Arabic-Indic Digits,
#           Katakana Middle Dot.
_IANA_CONTEXTJ_RANGES: list[str] = ["200C-200D"]
_IANA_CONTEXTO_RANGES: list[str] = [
    "00B7", "0375", "05F3-05F4", "0660-0669", "06F0-06F9", "30FB",
]

UNICODE_VALID: str = _expand_iana_ranges(
    _IANA_PVALID_RANGES + _IANA_CONTEXTJ_RANGES + _IANA_CONTEXTO_RANGES
)


# ---------------------------------------------------------------------------
# UNICODE_UNASSIGNED — code points with property UNASSIGNED in IANA IDNA 6.3.0
# Source: https://www.iana.org/assignments/idna-tables-6.3.0/idna-tables-6.3.0.xhtml
# ---------------------------------------------------------------------------

_IANA_UNASSIGNED_RANGES: list[str] = [
    "0378-0379", "037F-0383", "038B", "038D", "03A2", "0528-0530",
    "0557-0558", "0560", "0588", "058B-058E", "0590", "05C8-05CF",
    "05EB-05EF", "05F5-05FF", "0605", "061D", "070E", "074B-074C",
    "07B2-07BF", "07FB-07FF", "082E-082F", "083F", "085C-085D",
    "085F-089F", "08A1", "08AD-08E3", "08FF", "0978", "0980", "0984",
    "098D-098E", "0991-0992", "09A9", "09B1", "09B3-09B5",
    "09BA-09BB", "09C5-09C6", "09C9-09CA", "09CF-09D6", "09D8-09DB",
    "09DE", "09E4-09E5", "09FC-0A00", "0A04", "0A0B-0A0E",
    "0A11-0A12", "0A29", "0A31", "0A34", "0A37", "0A3A-0A3B", "0A3D",
    "0A43-0A46", "0A49-0A4A", "0A4E-0A50", "0A52-0A58", "0A5D",
    "0A5F-0A65", "0A76-0A80", "0A84", "0A8E", "0A92", "0AA9", "0AB1",
    "0AB4", "0ABA-0ABB", "0AC6", "0ACA", "0ACE-0ACF", "0AD1-0ADF",
    "0AE4-0AE5", "0AF2-0B00", "0B04", "0B0D-0B0E", "0B11-0B12",
    "0B29", "0B31", "0B34", "0B3A-0B3B", "0B45-0B46", "0B49-0B4A",
    "0B4E-0B55", "0B58-0B5B", "0B5E", "0B64-0B65", "0B78-0B81",
    "0B84", "0B8B-0B8D", "0B91", "0B96-0B98", "0B9B", "0B9D",
    "0BA0-0BA2", "0BA5-0BA7", "0BAB-0BAD", "0BBA-0BBD", "0BC3-0BC5",
    "0BC9", "0BCE-0BCF", "0BD1-0BD6", "0BD8-0BE5", "0BFB-0C00",
    "0C04", "0C0D", "0C11", "0C29", "0C34", "0C3A-0C3C", "0C45",
    "0C49", "0C4E-0C54", "0C57", "0C5A-0C5F", "0C64-0C65",
    "0C70-0C77", "0C80-0C81", "0C84", "0C8D", "0C91", "0CA9", "0CB4",
    "0CBA-0CBB", "0CC5", "0CC9", "0CCE-0CD4", "0CD7-0CDD", "0CDF",
    "0CE4-0CE5", "0CF0", "0CF3-0D01", "0D04", "0D0D", "0D11",
    "0D3B-0D3C", "0D45", "0D49", "0D4F-0D56", "0D58-0D5F",
    "0D64-0D65", "0D76-0D78", "0D80-0D81", "0D84", "0D97-0D99",
    "0DB2", "0DBC", "0DBE-0DBF", "0DC7-0DC9", "0DCB-0DCE", "0DD5",
    "0DD7", "0DE0-0DF1", "0DF5-0E00", "0E3B-0E3E", "0E5C-0E80",
    "0E83", "0E85-0E86", "0E89", "0E8B-0E8C", "0E8E-0E93", "0E98",
    "0EA0", "0EA4", "0EA6", "0EA8-0EA9", "0EAC", "0EBA", "0EBE-0EBF",
    "0EC5", "0EC7", "0ECE-0ECF", "0EDA-0EDB", "0EE0-0EFF", "0F48",
    "0F6D-0F70", "0F98", "0FBD", "0FCD", "0FDB-0FFF",
    "10C6", "10C8-10CC", "10CE-10CF", "1249", "124E-124F", "1257",
    "1259", "125E-125F", "1289", "128E-128F", "12B1", "12B6-12B7",
    "12BF", "12C1", "12C6-12C7", "12D7", "1311", "1316-1317",
    "135B-135C", "137D-137F", "139A-139F", "13F5-13FF", "169D-169F",
    "16F1-16FF", "170D", "1715-171F", "1737-173F", "1754-175F",
    "176D", "1771", "1774-177F", "17DE-17DF", "17EA-17EF",
    "17FA-17FF", "180F", "181A-181F", "1878-187F", "18AB-18AF",
    "18F6-18FF", "191D-191F", "192C-192F", "193C-193F", "1941-1943",
    "196E-196F", "1975-197F", "19AC-19AF", "19CA-19CF", "19DB-19DD",
    "1A1C-1A1D", "1A5F", "1A7D-1A7E", "1A8A-1A8F", "1A9A-1A9F",
    "1AAE-1AFF", "1B4C-1B4F", "1B7D-1B7F", "1BF4-1BFB", "1C38-1C3A",
    "1C4A-1C4C", "1C80-1CBF", "1CC8-1CCF", "1CF7-1CFF", "1DE7-1DFB",
    "1F16-1F17", "1F1E-1F1F", "1F46-1F47", "1F4E-1F4F", "1F58",
    "1F5A", "1F5C", "1F5E", "1F7E-1F7F", "1FB5", "1FC5", "1FD4-1FD5",
    "1FDC", "1FF0-1FF1", "1FF5", "1FFF", "2065", "2072-2073", "208F",
    "209D-209F", "20BB-20CF", "20F1-20FF", "218A-218F", "23F4-23FF",
    "2427-243F", "244B-245F", "2700", "2B4D-2B4F", "2B5A-2BFF",
    "2C2F", "2C5F", "2CF4-2CF8", "2D26", "2D28-2D2C", "2D2E-2D2F",
    "2D68-2D6E", "2D71-2D7E", "2D97-2D9F", "2DA7", "2DAF", "2DB7",
    "2DBF", "2DC7", "2DCF", "2DD7", "2DDF", "2E3C-2E7F", "2E9A",
    "2EF4-2EFF", "2FD6-2FEF", "2FFC-2FFF", "3040", "3097-3098",
    "3100-3104", "312E-3130", "318F", "31BB-31BF", "31E4-31EF",
    "321F", "32FF", "4DB6-4DBF", "9FCD-9FFF", "A48D-A48F",
    "A4C7-A4CF", "A62C-A63F", "A698-A69E", "A6F8-A6FF", "A78F",
    "A794-A79F", "A7AB-A7F7", "A82C-A82F", "A83A-A83F", "A878-A87F",
    "A8C5-A8CD", "A8DA-A8DF", "A8FC-A8FF", "A954-A95E", "A97D-A97F",
    "A9CE", "A9DA-A9DD", "A9E0-A9FF", "AA37-AA3F", "AA4E-AA4F",
    "AA5A-AA5B", "AAC3-AADA", "AAF7-AB00", "AB07-AB08", "AB0F-AB10",
    "AB17-AB1F", "AB27", "AB2F-ABBF", "ABEE-ABEF", "ABFA-ABFF",
    "D7A4-D7AF", "D7C7-D7CA", "D7FC-D7FF", "FA6E-FA6F", "FADA-FAFF",
    "FB07-FB12", "FB18-FB1C", "FB37", "FB3D", "FB3F", "FB42", "FB45",
    "FBC2-FBD2", "FD40-FD4F", "FD90-FD91", "FDC8-FDCF", "FDFE-FDFF",
    "FE1A-FE1F", "FE27-FE2F", "FE53", "FE67", "FE6C-FE6F", "FE75",
    "FEFD-FEFE", "FF00", "FFBF-FFC1", "FFC8-FFC9", "FFD0-FFD1",
    "FFD8-FFD9", "FFDD-FFDF", "FFE7", "FFEF-FFF8",
    "1000C", "10027", "1003B", "1003E", "1004E-1004F", "1005E-1007F",
    "100FB-100FF", "10103-10106", "10134-10136", "1018B-1018F",
    "1019C-101CF", "101FE-1027F", "1029D-1029F", "102D1-102FF",
    "1031F", "10324-1032F", "1034B-1037F", "1039E", "103C4-103C7",
    "103D6-103FF", "1049E-1049F", "104AA-107FF", "10806-10807",
    "10809", "10836", "10839-1083B", "1083D-1083E", "10856",
    "10860-108FF", "1091C-1091E", "1093A-1093E", "10940-1097F",
    "109B8-109BD", "109C0-109FF", "10A04", "10A07-10A0B", "10A14",
    "10A18", "10A34-10A37", "10A3B-10A3E", "10A48-10A4F",
    "10A59-10A5F", "10A80-10AFF", "10B36-10B38", "10B56-10B57",
    "10B73-10B77", "10B80-10BFF", "10C49-10E5F", "10E7F-10FFF",
    "1104E-11051", "11070-1107F", "110C2-110CF", "110E9-110EF",
    "110FA-110FF", "11135", "11144-1117F", "111C9-111CF",
    "111DA-1167F", "116B8-116BF", "116CA-11FFF", "1236F-123FF",
    "12463-1246F", "12474-12FFF", "1342F-167FF", "16A39-16EFF",
    "16F45-16F4F", "16F7F-16F8E", "16FA0-1AFFF", "1B002-1CFFF",
    "1D0F6-1D0FF", "1D127-1D128", "1D1DE-1D1FF", "1D246-1D2FF",
    "1D357-1D35F", "1D372-1D3FF", "1D455", "1D49D", "1D4A0-1D4A1",
    "1D4A3-1D4A4", "1D4A7-1D4A8", "1D4AD", "1D4BA", "1D4BC", "1D4C4",
    "1D506", "1D50B-1D50C", "1D515", "1D51D", "1D53A", "1D53F",
    "1D545", "1D547-1D549", "1D551", "1D6A6-1D6A7", "1D7CC-1D7CD",
    "1D800-1EDFF", "1EE04", "1EE20", "1EE23", "1EE25-1EE26", "1EE28",
    "1EE33", "1EE38", "1EE3A", "1EE3C-1EE41", "1EE43-1EE46", "1EE48",
    "1EE4A", "1EE4C", "1EE50", "1EE53", "1EE55-1EE56", "1EE58",
    "1EE5A", "1EE5C", "1EE5E", "1EE60", "1EE63", "1EE65-1EE66",
    "1EE6B", "1EE73", "1EE78", "1EE7D", "1EE7F", "1EE8A",
    "1EE9C-1EEA0", "1EEA4", "1EEAA", "1EEBC-1EEEF", "1EEF2-1EFFF",
    "1F02C-1F02F", "1F094-1F09F", "1F0AF-1F0B0", "1F0BF-1F0C0",
    "1F0D0", "1F0E0-1F0FF", "1F10B-1F10F", "1F12F", "1F16C-1F16F",
    "1F19B-1F1E5", "1F203-1F20F", "1F23B-1F23F", "1F249-1F24F",
    "1F252-1F2FF", "1F321-1F32F", "1F336", "1F37D-1F37F",
    "1F394-1F39F", "1F3C5", "1F3CB-1F3DF", "1F3F1-1F3FF", "1F43F",
    "1F441", "1F4F8", "1F4FD-1F4FF", "1F53E-1F53F", "1F544-1F54F",
    "1F568-1F5FA", "1F641-1F644", "1F650-1F67F", "1F6C6-1F6FF",
    "1F774-1FFFD", "2A6D7-2A6FF", "2B735-2B73F", "2B81E-2F7FF",
    "2FA1E-2FFFD", "30000-3FFFD", "40000-4FFFD", "50000-5FFFD",
    "60000-6FFFD", "70000-7FFFD", "80000-8FFFD", "90000-9FFFD",
    "A0000-AFFFD", "B0000-BFFFD", "C0000-CFFFD", "D0000-DFFFD",
    "E0000", "E0002-E001F", "E0080-E00FF", "E01F0-EFFFD",
]

UNICODE_UNASSIGNED: str = _expand_iana_ranges(_IANA_UNASSIGNED_RANGES)


# ---------------------------------------------------------------------------
# UNICODE_RESERVED — Private Use Area code points.
# The IANA IDNA 6.3.0 tables do not have an explicit "RESERVED" category;
# these are the BMP and supplementary private-use areas (Unicode category Co).
# ---------------------------------------------------------------------------

_RESERVED_RANGES: list[str] = [
    "E000-F8FF",        # BMP Private Use Area
    "F0000-FFFFD",      # Supplementary Private Use Area-A
    "100000-10FFFD",    # Supplementary Private Use Area-B
]

UNICODE_RESERVED: str = _expand_iana_ranges(_RESERVED_RANGES)


# ---------------------------------------------------------------------------
# UNICODE_DISALLOWED — every code point marked DISALLOWED in the IANA IDNA
# tables for Unicode 6.3.0.
# Source: https://www.iana.org/assignments/idna-tables-6.3.0/idna-tables-6.3.0.xhtml
# ---------------------------------------------------------------------------

_IANA_DISALLOWED_RANGES: list[str] = [
    "0000-002C", "002E-002F", "003A-0060", "007B-00B6", "00B8-00DE",
    "00F7",
    "0100", "0102", "0104", "0106", "0108", "010A", "010C", "010E",
    "0110", "0112", "0114", "0116", "0118", "011A", "011C", "011E",
    "0120", "0122", "0124", "0126", "0128", "012A", "012C", "012E",
    "0130", "0132-0134", "0136", "0139", "013B", "013D", "013F-0141",
    "0143", "0145", "0147", "0149-014A", "014C", "014E", "0150", "0152",
    "0154", "0156", "0158", "015A", "015C", "015E", "0160", "0162",
    "0164", "0166", "0168", "016A", "016C", "016E", "0170", "0172",
    "0174", "0176", "0178-0179", "017B", "017D", "017F",
    "0181-0182", "0184", "0186-0187", "0189-018B", "018E-0191",
    "0193-0194", "0196-0198", "019C-019D", "019F-01A0", "01A2", "01A4",
    "01A6-01A7", "01A9", "01AC", "01AE-01AF", "01B1-01B3", "01B5",
    "01B7-01B8", "01BC", "01C4-01CD", "01CF", "01D1", "01D3", "01D5",
    "01D7", "01D9", "01DB", "01DE", "01E0", "01E2", "01E4", "01E6",
    "01E8", "01EA", "01EC", "01EE", "01F1-01F4", "01F6-01F8", "01FA",
    "01FC", "01FE",
    "0200", "0202", "0204", "0206", "0208", "020A", "020C", "020E",
    "0210", "0212", "0214", "0216", "0218", "021A", "021C", "021E",
    "0220", "0222", "0224", "0226", "0228", "022A", "022C", "022E",
    "0230", "0232", "023A-023B", "023D-023E", "0241", "0243-0246",
    "0248", "024A", "024C", "024E",
    "02B0-02B8", "02C2-02C5", "02D2-02EB", "02ED", "02EF-02FF",
    "0340-0341", "0343-0345", "034F",
    "0370", "0372", "0374", "037A", "037E", "0384-038A", "038C",
    "038E-038F", "03CF-03D6", "03D8", "03DA", "03DC", "03DE", "03E0",
    "03E2", "03E4", "03E6", "03E8", "03EA", "03EC", "03EE",
    "03F0-03F2", "03F4-03F7", "03F9-03FA", "03FD-042F",
    "0460", "0462", "0464", "0466", "0468", "046A", "046C", "046E",
    "0470", "0472", "0474", "0476", "0478", "047A", "047C", "047E",
    "0480", "0482", "0488-048A", "048C", "048E",
    "0490", "0492", "0494", "0496", "0498", "049A", "049C", "049E",
    "04A0", "04A2", "04A4", "04A6", "04A8", "04AA", "04AC", "04AE",
    "04B0", "04B2", "04B4", "04B6", "04B8", "04BA", "04BC", "04BE",
    "04C0-04C1", "04C3", "04C5", "04C7", "04C9", "04CB", "04CD",
    "04D0", "04D2", "04D4", "04D6", "04D8", "04DA", "04DC", "04DE",
    "04E0", "04E2", "04E4", "04E6", "04E8", "04EA", "04EC", "04EE",
    "04F0", "04F2", "04F4", "04F6", "04F8", "04FA", "04FC", "04FE",
    "0500", "0502", "0504", "0506", "0508", "050A", "050C", "050E",
    "0510", "0512", "0514", "0516", "0518", "051A", "051C", "051E",
    "0520", "0522", "0524", "0526",
    "0531-0556", "055A-055F", "0587", "0589-058A", "058F",
    "05BE", "05C0", "05C3", "05C6", "05F3-05F4",
    "0600-0604", "0606-060F", "061B-061C", "061E-061F", "0640",
    "0675-0678", "06D4", "06DD-06DE", "06E9",
    "0700-070D", "070F", "074D-07B1",
    "082E-082F", "0830-083E", "085E", "08E4-08FE",
    "0958-095F", "0964-0965", "0970", "0978",
    "1100-11FF", "109E-10C5", "10C7", "10CD", "10FB-10FC",
    "1360-137C", "1390-1399", "1400", "166D-166E", "1680",
    "169B-169C", "16EB-16F0", "1735-1736", "17B4-17B5",
    "17D4-17D6", "17D8-17DB", "17F0-17F9",
    "1800-180E", "1878-187F", "18AB-18AF", "18F6-18FF",
    "191D-191F", "192C-192F", "193C-193F", "1940", "1944-1945",
    "196E-196F", "1975-197F", "19AC-19AF", "19DA", "19DE-19FF",
    "1A1E-1A1F", "1A5F", "1A8A-1A8F", "1AA0-1AA6", "1AA8-1AAD",
    "1AAE-1AFF", "1B4C-1B4F", "1B5A-1B6A", "1B74-1B7C", "1B7D-1B7F",
    "1BFC-1BFF", "1C3B-1C3F", "1C4A-1C4C", "1C7E-1C7F",
    "1CC0-1CC7", "1CD3", "1CF7-1CFF",
    "1D2C-1D2E", "1D30-1D3A", "1D3C-1D4D", "1D4F-1D6A", "1D78",
    "1D9B-1DBF", "1DFC-1DFF",
    "1E00", "1E02", "1E04", "1E06", "1E08", "1E0A", "1E0C", "1E0E",
    "1E10", "1E12", "1E14", "1E16", "1E18", "1E1A", "1E1C", "1E1E",
    "1E20", "1E22", "1E24", "1E26", "1E28", "1E2A", "1E2C", "1E2E",
    "1E30", "1E32", "1E34", "1E36", "1E38", "1E3A", "1E3C", "1E3E",
    "1E40", "1E42", "1E44", "1E46", "1E48", "1E4A", "1E4C", "1E4E",
    "1E50", "1E52", "1E54", "1E56", "1E58", "1E5A", "1E5C", "1E5E",
    "1E60", "1E62", "1E64", "1E66", "1E68", "1E6A", "1E6C", "1E6E",
    "1E70", "1E72", "1E74", "1E76", "1E78", "1E7A", "1E7C", "1E7E",
    "1E80", "1E82", "1E84", "1E86", "1E88", "1E8A", "1E8C", "1E8E",
    "1E90", "1E92", "1E94", "1E9A-1E9B", "1E9E",
    "1EA0", "1EA2", "1EA4", "1EA6", "1EA8", "1EAA", "1EAC", "1EAE",
    "1EB0", "1EB2", "1EB4", "1EB6", "1EB8", "1EBA", "1EBC", "1EBE",
    "1EC0", "1EC2", "1EC4", "1EC6", "1EC8", "1ECA", "1ECC", "1ECE",
    "1ED0", "1ED2", "1ED4", "1ED6", "1ED8", "1EDA", "1EDC", "1EDE",
    "1EE0", "1EE2", "1EE4", "1EE6", "1EE8", "1EEA", "1EEC", "1EEE",
    "1EF0", "1EF2", "1EF4", "1EF6", "1EF8", "1EFA", "1EFC", "1EFE",
    "1F08-1F0F", "1F18-1F1D", "1F28-1F2F", "1F38-1F3F", "1F48-1F4D",
    "1F59", "1F5B", "1F5D", "1F5F", "1F68-1F6F",
    "1F71", "1F73", "1F75", "1F77", "1F79", "1F7B", "1F7D",
    "1F80-1FAF", "1FB2-1FB4", "1FB7-1FC4", "1FD3", "1FD8-1FDB",
    "1FDD-1FDF", "1FE3", "1FE8-1FEF", "1FF2-1FF4", "1FF7-1FFE",
    "2000-200B", "200E-2064", "2066-2071", "2074-208E", "2090-209C",
    "20A0-20BA", "20D0-20F0",
    "2100-214D", "2185-2189", "2190-23F3", "2400-2426", "2440-244A",
    "2460-26FF", "2701-2B4C", "2B50-2B59",
    "2C00-2C2E", "2C60", "2C62-2C64", "2C67", "2C69", "2C6B",
    "2C6D-2C70", "2C72", "2C75", "2C7C-2C80",
    "2C82", "2C84", "2C86", "2C88", "2C8A", "2C8C", "2C8E",
    "2C90", "2C92", "2C94", "2C96", "2C98", "2C9A", "2C9C", "2C9E",
    "2CA0", "2CA2", "2CA4", "2CA6", "2CA8", "2CAA", "2CAC", "2CAE",
    "2CB0", "2CB2", "2CB4", "2CB6", "2CB8", "2CBA", "2CBC", "2CBE",
    "2CC0", "2CC2", "2CC4", "2CC6", "2CC8", "2CCA", "2CCC", "2CCE",
    "2CD0", "2CD2", "2CD4", "2CD6", "2CD8", "2CDA", "2CDC", "2CDE",
    "2CE0", "2CE2", "2CE5-2CEB", "2CED", "2CF2", "2CF9-2CFF",
    "2D6F-2D70",
    "2E00-2E2E", "2E30-2E3B",
]


UNICODE_DISALLOWED: str = _expand_iana_ranges(_IANA_DISALLOWED_RANGES)