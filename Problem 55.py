def miroir(n):  #renverse un nombre en miroir
    puiss=-1
    a=n
    b=n
    inverse=0
    while b!=0:
        b=b//10
        puiss+=1
    while a!=0:
        inverse+=a%10*(10**puiss)
        puiss=puiss-1
        a=a//10
    return inverse

def egal_a_son_miroir (n): #teste si un nombre et son miroir sont égaux, ie si le nombre est un palindrome
    mir=miroir(n)
    return mir==n


def  is_palindromic (n): #teste si un nombre est "palindromic"
    k=1
    a=n+miroir(n)
    while k<=50:
        if egal_a_son_miroir(a):
            return True
        a=a+miroir(a)
        k+=1
    return False
 
assert(is_palindromic(4994)== False)

def Lychrel_numbers_below(n): #renvoie le nombre de nombres de Lychrel en dessous de n
    total=0
    for k in range(n+1):
        if not is_palindromic(k):
            total+=1
    return total

print( Lychrel_numbers_below(10000))
  
    