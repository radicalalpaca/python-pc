
def lcm(a,b):
    for i in range (2, (a*b)+1):
        if i%a==0 and i%b==0:
            print(i)
            break
    
