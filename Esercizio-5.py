def primo(k):
    for y in range (2, k):
        check = int(k/y)
        if check * y == k:
            return False
        
    return True

######
k = int(input("Inserisci un numero: "))   
print(primo(k))
######