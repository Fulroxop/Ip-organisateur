import os

def binform(x):
    return int(bin(x)[2:])

choix=input("1 pour trouver l'ip du reseaux, 2 pour crée un resaux selon le nombre de personnes necessaire ")
try:
    if choix not in ["2","1"]:
        raise ValueError
except ValueError:
    print("vous n'avez pas choisie entre 1 et 2")


binadresse=""
binmask=""
adrs_resaux=""
bro_cast=""
mask_resaux=""
mask_inverser=""
mask=""


if choix == "1":
    ipadresse=input("quel est l'adresse ip ? ")
    mask=input("quel est le masque de reseau ? ")

    for i in ipadresse.split("."):
        binadresse+=str(binform(int(i))).zfill(8)
    for i in mask.split("."):
        binmask+=str(binform(int(i))).zfill(8)
    for i in mask.split("."):
        mask_inverser+=str(binform(255-int(i))).zfill(8)
    
    zeromask=binmask.count("0")
    
    
    adrs_binresaux=binform(int(binadresse,2) & int(binmask,2))
    adrs_bincast=binform(int(str(adrs_binresaux),2) | int(mask_inverser,2))

    
    for i in range(0,4):
        adrs_resaux+=str(int(str(adrs_binresaux)[8*(i):8*(i+1)],2))+"."

    for i in range(0,4):
        bro_cast+=str(int(str(adrs_bincast)[8*(i):8*(i+1)],2))+"."
    
   
    print("L'adresse resaux est: "+adrs_resaux[:-1])
    print("L'adresse de brodcast est: "+bro_cast[:-1])
    print("Vous pouvez connecter",2**zeromask-2,"machine sur le resaux")

elif choix == "2":

    ipadresse=input("votre adresse ip ")
    personne=input("combien de personne dans votre reseau ? ")
    zeromask=0

    while 2**zeromask < int(personne):
        zeromask+=1
  
    binmask+=str(1)*(32-zeromask)+str(0)*zeromask

    for i in range(0,4):
        mask+=str(int(str(binmask)[8*(i):8*(i+1)],2))+"."

    mask=mask[:-1]

    for i in ipadresse.split("."):
        binadresse+=str(binform(int(i))).zfill(8)
    for i in mask.split("."):
        mask_inverser+=str(binform(255-int(i))).zfill(8)


    adrs_binresaux=binform(int(binadresse,2) & int(binmask,2))
    adrs_bincast=binform(int(str(adrs_binresaux),2) | int(mask_inverser,2))

    
    for i in range(0,4):
        adrs_resaux+=str(int(str(adrs_binresaux)[8*(i):8*(i+1)],2))+"."

    for i in range(0,4):
        bro_cast+=str(int(str(adrs_bincast)[8*(i):8*(i+1)],2))+"."
    
   
    print("L'adresse resaux est: "+adrs_resaux[:-1])
    print("L'adresse de brodcast est: "+bro_cast[:-1])
    print("Vous pouvez connecter",2**zeromask-2,"machine sur le resaux")
    

os.system("pause")