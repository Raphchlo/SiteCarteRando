# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 17:08:22 2025

@author: maxime.vernay
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(open("randoscrap.html"),features="html.parser")

print(soup.prettify())

print(soup.title)