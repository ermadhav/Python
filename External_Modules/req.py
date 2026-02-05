# import requests
# r = requests.get('https://api.github.com/users/ermadhav')
# print(r.text)
# with open("ermadhav.txt", "w") as f:
#     f.write(r.text)

import re
text = "Madhav is a genius Boy,Madhav loves space and coding"
matches = re.findall("Madhav", text, re.IGNORECASE)
print(matches)