
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b, a%b)


def totient(n):
    count=0
    for m in range(1,n):
        if hcf(m,n)==1:
            count+=1
    print(count)
