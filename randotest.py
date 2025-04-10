# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 17:08:22 2025

@author: maxime.vernay
"""
import urllib.parse
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("randoscrap.html"),features="html.parser")
 



for link in soup.find_all('a'):
    href = "https://randogps.net" + link.get('href')[2:-1]
    href = href.replace(' ', '-')
    print(href)
    res = urllib.request.urlopen(href)
    data = res.read()
soup2 = BeautifulSoup(open(data),features="html.parser")
for link2 in soup2.find_all('a'):
    print(link2)




#print("result code:" +str(res.getcode()))
#soup2 = BeautifulSoup(open(data),features="html.parser")
#parseRes = urllib.parse.urlsplit(href)
#print(parseRes)
#print(urllib.parse.parse_qs(parseRes.query) )

#f = urllib.urlopen(href)
#print(BeautifulSoup(open(f),features="html.parser"))

