def Numeri(lista):
    #lista = [3, 7, 9, 5]    
    for num in lista :
        output = ""
        for x in range(0, num):
            output = output + "*"
        print(output)
        
fabio = []
quest = int(input("Quanti numeri devo stampare: "))
for x in range(0,quest):
    y = int(input("Numero desiderato "))
    fabio.append(y)
Numeri(fabio)
