import requests
import time
import json
r=requests.get('https://api.github.com')
print(r.text)## comes in string
ofile=json.loads(r.text)## json format
print(ofile)
for i in ofile:
    print(i)
    print(ofile[i])


