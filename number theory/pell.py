from time import process_time


def pell(n,m):
    t = process_time()
    for i in range (1,m):
        for j in range (1,m):
            if i*i-n*j*j==1:
                print(i,j)
    elapsed_time = process_time() - t
    print("time taken:",elapsed_time)
    
