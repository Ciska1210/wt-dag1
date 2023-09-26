print("Start api readapplication")

import requests

paginaresults = requests.get('https://catfact.ninja/facts')
print(paginaresults)

feitjes = paginaresults.json()
print(feitjes["current_page"])
print(feitjes["data"][0]["fact"])