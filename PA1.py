import time
#Measures speed of recursive fib function
#results posted on PA1 word doc

def rec_fib(n):
    if n < 2:
        return n
    else:
        return rec_fib(n-1)+rec_fib(n-2)

def fib_non(n):
    a = 0
    b = 1
    if n<2:
        return n
    else:
        for x in range(2, n+1):
            c = a+b
            a = b
            b = c
        return b
    
for x in range(0,36):
    print(x)
    for y in range(20):
        time_rec = time.perf_counter()
        for _ in range(50):
            var = fib_non(x)
        average = (time.perf_counter() - time_rec)/50
        print("{:12.10f}".format(average))

for x in range(0,20):
    print(x)
    for y in range(20):
        time_rec = time.perf_counter()
        for _ in range(50):
            var = rec_fib(x)
        average = (time.perf_counter() - time_rec)/50
        print("{:12.10f}".format(average))
    
    

#print(rec_fib(19))
#print(input("any key"))
