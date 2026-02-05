import requests
r = requests.get('https://api.github.com/users/ermadhav')
print(r.text)
with open("ermadhav.txt", "w") as f:
    f.write(r.text)