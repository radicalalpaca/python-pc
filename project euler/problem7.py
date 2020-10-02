import math

def sieve(n):
    a = []
    prime = [True for i in range(n+1)]
    p = 2

    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False

    for p in range(n+1):
        if prime[p]:
            a.append(p)
        elif len(a) == 10001:
            print(p-1)
            break

    print(a)
    print(len(a))

    
        

    
            
                
    
