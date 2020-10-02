
def lindio(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i+5*j==50:
                print(i,j)


def solve(a,b,n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a*i+b*j==n:
                print(i,j)
