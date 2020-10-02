def palcheck(n):
    temp = n
    rev = 0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if(temp == rev):
        return True
    else:
        return False

def pal(n):
    a = []
    for i in range(10 ** (n-1), 10 ** n):
        for j in range(10 ** (n-1), 10 ** n):
            if palcheck(i * j) == True:
                a.append(i*j)
            else:
                pass
    print(max(a))
            
        


        
