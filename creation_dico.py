import urllib.parse
dico = {}
fichier  = open("randogps38 (2).odt")
fichier_lien = open("lien_fichier_gpx.txt")

#~~~~~~~~~~~~~~~~~~rajout des clés du dico
for lien in fichier_lien :
    num=lien.split('=')[2][:-5]
    #print(lien.split('=')[2][])
    dico[num]=[]
    res = urllib.request.urlopen(lien)
    data = str(res.read()).split("<")
    fichiertemp = open("gpx.gpx","w+")
    fichiertemp.write(str(data))
    fichiertemp.close()
    fichiertemp = open("gpx.gpx","r")
    

    texte=fichiertemp.readlines()
   
    fichiertemp.close()
    a=texte[0].split(" ")
    for element in a :
        if "minlat=" in element: 
            #print(element)
            lat= element.split('"')[1]
        if "minlon=" in element: 
            #print(element)
            lon= element.split('"')[1]
            pass

    #print(lat.split(" "))

    #print(long)
    coordonée=(lat,lon)
    print(coordonée)
    if coordonée != () :
        dico[num].append(coordonée)
    else :
        del dico[num]



#~~~~~~~~~~~~~~~~~~ajout des donnés dans le dico
n = 0
cleact = 0
for ligne in fichier :
    donnée =  ligne.split('"')
    if n>=11303 and n<20693:
        if (n-11303)%5==0:       
            cleact = donnée[1]
        elif (n-11304)%5==0 and cleact in dico.keys() :
            dico[cleact].append(donnée[1])
        elif (n-11305)%5==0 and cleact in dico.keys():
            dico[cleact].append(donnée[1])
        elif (n-11306)%5==0 and cleact in dico.keys():
            dico[cleact].append(donnée[1])
        elif (n-11307)%5==0 and cleact in dico.keys():
            dico[cleact].append(donnée[1])
    n+=1
 #~~~~~~~~~~~~~~~~ajout des coordonnées dans le dico   
