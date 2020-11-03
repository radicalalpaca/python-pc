import random
import matplotlib.pyplot as plt

#Ex 6A
def EstimateSuperEllipse(m,n):
    random.seed(1234)
    i = 0
    hits = 0
    for j in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        i += 1
        if abs(x) ** m + abs(y) ** m < 1:
            hits += 1
        else:
            continue
    return (hits / i) * 4


#Ex6B
#1
def laggedfib(j,k,m,initlist,n):
    sequence = initlist
    for i in range(k, k + n):
        sequence.append((sequence[i-j] + sequence[i-k]) % m)
    return sequence[k:]


#2
#Write your code to produce the lagged Fibonacci figure here.
#The graph should appear when the file is run.
x = laggedfib(7, 10, 2**32, 10*[1], 2000)

#3
#Write your code to produce your Mersenne Twister figure here.
#The graph should appear when the file is run.


#4
#def arithmeticmean(sequence,hi,lo):

    
#5 Write your comment below.