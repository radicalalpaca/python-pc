
def fermat(n):
    for x in range(1,100):
        for y in range(1,100):
            for z in range(1,100):
                if (x**n)+(y**n)==(z**n):
                    print(x,y,z)
