num_1 = int(input("Numero-1:"))
num_2 = int(input("Numero-2:"))
num_3 = int(input("Numero-3:"))
num_4 = int(input("Numero-4:"))
num_5 = int(input("Numero-5:"))
Lista = [num_1, num_2, num_3, num_4, num_5]
Lista.reverse()
for x in Lista:
    q = int(x/2)
    if q*2 == x:
        print(x)