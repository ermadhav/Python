import requests
r = requests.get('https://api.github.com/users/ermadhav')
print(r.text)