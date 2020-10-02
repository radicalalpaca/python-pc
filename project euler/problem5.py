import math

def lcm(n):
    r = 1
    for i in range(2,n+1):
        r = r * i // math.gcd(r,i)
    print(r)
        
