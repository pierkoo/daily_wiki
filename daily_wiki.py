import requests

r = requests.get('https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona')

with open('log.txt', 'w', encoding="utf-8") as open_file:
    open_file.write(r.text)



print(r.url)
