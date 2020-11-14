import urllib.parse
import sys

def encodeUrl(query):
    print(urllib.parse.quote(query, safe=""))
    print(urllib.parse.quote_plus(query, safe=""))

encodeUrl(str(sys.argv[1]))