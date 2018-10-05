
def puissance (a,n):
#calcule le nombre a à la puissance n
    var=1
    for k in range (n):
        var=a*var
    return var

def somme_chiffre (n): #programme donnant la somme des chiffres composant un nombre
    somme=0
    while n !=0:
        somme+=n%10
        n=n//10
    return somme 


def solve (a,n):
    nombre= puissance(a, n)
    return (somme_chiffre (nombre))


assert solve (2,15)==26
print(solve (2,1000))
