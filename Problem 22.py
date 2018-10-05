f  =  open("p022_names.txt")

for ligne in f:
    liste_intermediaire=ligne
    liste=liste_intermediaire.split(',')
    liste_finale=sorted(liste)
print (liste_finale)    


def somme_des_caracteres (chaine):#calcule la somme des valeurs des lettres composant un mot
    s=0
    for k in range(len(chaine)):
        s+=ord(chaine[k])-64
              
    return s

def valeur_totale_du_document (l):
    v=0
    for k in range(len(l)):
        l[k]=l[k].replace('"','')
        v+=(k+1)*somme_des_caracteres (l[k])
    return v
    
print(valeur_totale_du_document(liste_finale))


# si on prend la liste ["BABA","C"], la fonction valeur_totale_du_document doit retourner 1*(2+1+2+1)+2*3=12. Vérification:

print(valeur_totale_du_document(["BABA","C"]))