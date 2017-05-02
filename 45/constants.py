
def fib(x):
    a,b=0,1
    list = []
    list.append(a)
    while b<x:
        list.append(b)
        a,b = b,a+b
    print(list)



