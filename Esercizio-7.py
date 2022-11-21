def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


input = 10


for x in range(0,input):
    print(fib(x))
    