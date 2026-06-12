import urllib.request
import urllib.parse
import json

url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=fr&tl=en&dt=t'
text = "bonjour\n|||\nau revoir"
data = urllib.parse.urlencode({'q': text}).encode('utf-8')
req = urllib.request.Request(url, data=data)
try:
    response = urllib.request.urlopen(req).read().decode('utf-8')
    res = json.loads(response)[0]
    out = "".join(x[0] for x in res if x[0])
    print(out.split('\n|||\n'))
except Exception as e:
    print(e)
