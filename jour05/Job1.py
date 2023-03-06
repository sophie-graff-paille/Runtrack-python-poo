def factorielle(n): # n est un entier naturel (n >= 0)
    if n == 0: # cas de base de la récursivité (n = 0) 
        return 1 
    else:
        return n * factorielle(n-1) # appel récursif de la fonction factorielle