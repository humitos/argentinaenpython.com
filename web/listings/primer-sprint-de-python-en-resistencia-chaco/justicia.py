#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib import request

DOMAIN = 'http://www.justiciachaco.gov.ar'

response = request.urlopen(DOMAIN + '/listas/C_A_Civ_y_Com_Sala_I/')
html = response.read()
soup = BeautifulSoup(html)
a_tags = soup.find_all('a')

response = request.urlopen(DOMAIN + a_tags[-1].attrs['href'])
txt = response.read()
print(txt)
