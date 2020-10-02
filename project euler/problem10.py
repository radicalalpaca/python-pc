import math

def sieve(n):
    a = []
    prime = [True for i in range(n+1)]
    p = 2
    s = 0



    while (p ** 2 <= n):
        if (prime[p] == True):
            for i in range(p *  2, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False

    for p in range(n+1):
        if prime[p]:
            a.append(p)

    print(a)

    for i in a:
        s += i
    print(s)

    
