from time import process_time


def euler(n):
    t = process_time()
    for x in range (140,n):
        for y in range (140,n):
            for z in range (140,n):
                for w in range (140,n):
                    for j in range(140,n):
                        if (x**5)+(y**5)+(z**5)+(j**5)==(w**5):
                            print(x,y,z,j,w)
    elapsed_time = process_time() - t
    print("time taken:",elapsed_time)
