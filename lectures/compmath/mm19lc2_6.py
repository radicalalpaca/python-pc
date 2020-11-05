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
x_1 = laggedfib(7, 10, 2**32, 10*[1], 2000)
y_1 = x_1.copy()
y_1.append(x_1[0])
y_1.pop(0)

plt.scatter(x_1, y_1)
plt.show()
#3
#Write your code to produce your Mersenne Twister figure here.
#The graph should appear when the file is run.
x_2 = [random.randint(0, 2**32 - 1) for i in range(2000)]
y_2 = x_2.copy()
y_2.append(x_2[0])
y_2.pop(0)
plt.scatter(x_2, y_2)
plt.show()

def arithmeticmean(sequence,hi,lo):
    mean = sum(sequence) / len(sequence)
    midpoint = (hi + lo) / 2
    ratio = mean / midpoint
    return mean, midpoint, ratio

print(arithmeticmean(x_1, 2**32 - 1, 0))
print(arithmeticmean(x_2, 2**32 - 1, 0))

    
#5 Write your comment below.
# The mean of z_i is 2135295210.4195 while the mean of x_i is 1890192969.515. The ratio
# for x_i is 0.88, while for z_i it is 0.99, suggesting z_i is more random.