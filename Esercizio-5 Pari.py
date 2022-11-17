def pari(y):
    check = int(y/2)
    if check * 2 == y: return True
    else: return False




k = int(input("Inseirisci un numero: "))

ris = pari(k)

if ris == True: print("pari")
else: print ("dispari")