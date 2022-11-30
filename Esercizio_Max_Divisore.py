#def meccanismo(m):
 #   y = int(input("Quanti numeri devo stampare: "))
  #  for x in range(y):
   #     k = int(input(" Numero da inserire: "))
n1 = 9
n_ciclo = n1+1
n2 = 72

if n1>n2 : n_ciclo = n2+1
else: n_ciclo = n1+1

Lista = []
for x in reversed(range(2,n_ciclo)):
    check = int(n2/x)
    check2 = int(n1/x)
    if check * x == n2 and check2 * x == n1:
        Lista.append(x)

print(Lista)
