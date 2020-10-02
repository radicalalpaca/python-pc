
from time import process_time

def onemore(n):
    t = process_time()
    for x in range (2,n):
        for y in range (2,n):
            for m in range (1,n):
                if (x*x*x+y*y*y)-(m*m*m)==1:
                    print(x,y,m)
    elapsed_time = process_time()-t
    print("time taken:",elapsed_time)

def oneless(n):
    t = process_time()
    for x in range (2,n):
        for y in range (2,n):
            for m in range (1,n):
                if -(x*x*x+y*y*y)+(m*m*m)==1:
                    print(x,y,m)
    elapsed_time = process_time()-t
    print("time taken:",elapsed_time)
