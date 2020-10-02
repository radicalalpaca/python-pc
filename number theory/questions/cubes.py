
def cubes(n):
    for w in range (1,n):
        for x in range (1,n):
            for y in range (1,n):
                for z in range (1,n):
                    if w*w*w+x*x*x+y*y*y==z*z*z:
                        print(w,x,y,z)
