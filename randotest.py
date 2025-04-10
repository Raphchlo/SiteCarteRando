# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 17:08:22 2025

@author: maxime.vernay
"""
import urllib.parse
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("randoscrap.html"),features="html.parser", from_encoding='utf8')
 

def testparam(link):
    return link.get('href') and not 

def test(soup):

    for link in soup.find_all('a'):
        href = "https://randogps.net" + link.get('href')[2:-1]
        href = href.replace(' ', '-')
        print(href)
        res = urllib.request.urlopen(href)
        data = res.read()
        
        fichier = open("fichierEcriture.html", "a")
        fichier.write(str(data))
        fichier.close()
        soup2 = BeautifulSoup(open("fichierEcriture.html"),features="html.parser")
        print(soup.etat)
        for link2 in soup2.find_all("a"):
            if testparam(link2):
                href2 =link2.get("href")
                if href2[-1]=="2":
                    print(href2)
                print(" -      ok      -")
            return
        for link2 in soup2.find_all("a"):
            href2 =link2.get("href")
            if href2[-1]=="2":
                print(href2)
            print(" -      ok      -")
            return
    #try:
        #res = urllib.request.urlopen(href)
        #data = res.read()
    #except:
     #pass
   
#soup2 = BeautifulSoup(open(href),features="html.parser")
#for link2 in soup2.find_all('a'):
    #print(link2)

test(soup)


#print("result code:" +str(res.getcode()))
#soup2 = BeautifulSoup(open(data),features="html.parser")
#parseRes = urllib.parse.urlsplit(href)
#print(parseRes)
#print(urllib.parse.parse_qs(parseRes.query) )

#f = urllib.urlopen(href)
#print(BeautifulSoup(open(f),features="html.parser"))

