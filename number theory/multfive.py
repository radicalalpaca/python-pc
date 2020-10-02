
def multfive(n):
    m=5*n
    print(m)

def fivemults(n):
    for i in range (1,n):
        if i%5==0:
            print(i)

def fiveone(n):
    if n%5==1:
        return(1)
    else:
        return(0)

def squaresfiveone(n):
    output=0
    for i in range (1,n+1):
        output+=fiveone(i*i)
    print(output)



    
