def solve(n):
    for a in range(1, n):
        for b in range(a+1,n):
            c = n - a - b
            if a*a + b*b == c*c:
                return a*b*c

