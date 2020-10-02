from time import process_time


def solve(n):
    t = process_time()
    for i in range(1,n,21):
        for j in range(1,n):
            if i*i*i==j*j+500:
                print("y =",i,"x =",j)
    elapsed_time = process_time() - t
    print("time taken:",elapsed_time)
    
