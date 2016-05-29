import sys

import requests  # fades

from bs4 import BeautifulSoup  # fades

for user in open(sys.argv[1], 'r').readlines():
    url = 'https://twitter.com/{}'.format(user[2:-2])
    data = requests.get(url).content
    soup = BeautifulSoup(data)
    img = soup.find('img', {'class': 'ProfileAvatar-image'})
    print(img.get('src'))
