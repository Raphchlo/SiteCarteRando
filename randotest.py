# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 17:08:22 2025

@author: maxime.vernay
"""
import urllib.parse
from bs4 import BeautifulSoup
""" import du module beautiful soup (bs3) afin de parcourir un fichier html et en retirer des informations utiles
et du module urllib afin de pouvoir ouvrir des lien https et récupérer le fichier html du site """



soup = BeautifulSoup(open("randoscrap.html"),features="html.parser", from_encoding='utf8')
 # ouverture avec bs3 du fichier principale du site de randonné a scraper que nous avons teechacger au préalable


def test(soup):
    """ Cette fonction a pour objectif de parcourir les pages du site de randonné et de récupérer et stocker le lien vers le fichier gpx des différentes randonnée
    /!\ les lien eregistrés sont sont des liens de téléchargement qui seront à enrgister tel quel dans la base de donnée"""
    n = 0
    for link in soup.find_all('a'): ## pour chauqe balise <a> de la page 
        n+=1
        print(str(n)+ "/1873" )
        href = "https://randogps.net" + link.get('href')[2:-1]  ## rajout du https au lien pour pouvoir l'ouvrr avec urllib
        href = href.replace(' ', '-')  ## on remplace les espaces par des tres pour éviter les bugs
        try :
            res = urllib.request.urlopen(href)  ## ouverture du lien avec urllib
        except:
            pass
        data = res.read()    ## lecture du fichier obtenu
        
        fichier = open("fichierEcriture.html", "w") ## ouvertre d'un fichier html créé au préalable 
        fichier.write(str(data))  # on enregistre la page html dans le fichier
        fichier.close()
        soup2 = BeautifulSoup(open("fichierEcriture.html"),features="html.parser")  ## on ouvre le fchier html ainsi obtnu avec bs3
        
        for link2 in soup2.find_all("a"):
            ##### on répette l'étape précédente une nouvelle fois avec la nouvele page
            href2 ="https://randogps.net/" + link2.get("href")
            if "param1" in href2:   # cette fois on seletionne les lien avec le mot 'param1' dedans car c'est ce ien qui nous intéresse

                href2 = href2.replace(' ', '-')
                try:
                   res = urllib.request.urlopen(href2)
                except:
                    pass
                data = res.read()
                fichier = open("fichierEcriture.html", "w")
                fichier.write(str(data))
                fichier.close()
                soup3 = BeautifulSoup(open("fichierEcriture.html"),features="html.parser")
                
                for link3 in soup3.find_all("a"):
                    
                    ## on répète l'etape une dernière fois, cete fois on va chercher les liens de téléchargement des fichier gpx
                    href3 = link3.get("href")
                    if "nb_telecharge" in href3 and "gpx" in href3:
                        ### on vérifie donc que e lien contient les mos clé 'nb_telecharge' et 'gpx' 
                        ### on peuyt change rle mot cle 'gpx par un autre nom d'extention pour obtenir un aure type de fichier
                       href3 = "https://randogps.net/" + href3
                       
                       # on ajoute e lien de téléchargement au fchier qui contendra tous les liens de téléchargement
                       fichier = open("lien_fichier_gpx.txt", "a")
                       fichier.write(str(href3)+'\n')
                       fichier.close()
    print(" -      ok      programme     terminé      -")
    return


test(soup)



