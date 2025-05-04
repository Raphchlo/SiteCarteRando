
dico = {}
fichier  = open("randogps38 (2).odt")
n = 0
cleact = 0
for ligne in fichier :
    donnée =  ligne.split('"')
    if n>=11303 and n<20693:
        if (n-11303)%5==0:       
            dico[donnée[1]] = []
            cleact = donnée[1]
        elif (n-11304)%5==0:
            dico[cleact].append(donnée[1])
        elif (n-11305)%5==0:
            dico[cleact].append(donnée[1])
        elif (n-11306)%5==0:
            dico[cleact].append(donnée[1])
        elif (n-11307)%5==0:
            dico[cleact].append(donnée[1])
    n+=1
print(dico)
    
    
