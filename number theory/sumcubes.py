from time import process_time

def sumcubes(n):
    t = process_time()
    for x in range(1,int(n**(1/3)+1)):
        for y in range(1,int(n**(1/3)+1)):
            for z in range(1,int(n**(1/3)+1)):
                if x*x*x+y*y*y+z*z*z==n:
                    print(x,y,z)
    elapsed_time = process_time() - t
    print("time taken:",elapsed_time)
