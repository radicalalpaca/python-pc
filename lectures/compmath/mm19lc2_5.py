
#Exercise 6A solutions 

#import modules here
import matplotlib.pyplot as plt
import numpy as np


#Exercise 6A(i)
def collatzseq(n):
    collatz = [n]
    i = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            collatz.append(n)
            i += 1
        else:
            n = 3 * n + 1
            collatz.append(n)
            i += 1
    return collatz


#Exercise 6A(ii)
def collatzcount(n):
    return len(collatzseq(n)) - 1


#Exercise 6A(iii)

#Write your code that plots your graph here (not commented out)
x_list = [i for i in range(1, 1001)]
y_list = [collatzcount(i) for i in x_list]
plt.xlabel("n")
plt.ylabel("S(n)")
plt.scatter(x_list, y_list, marker=".")
plt.show()
    
#Exercise 6A(iv)

# 44.3 %
# i = 0
# for x in x_list:
#     if collatzcount(x) < x / 10:
#         i += 1
# print(i / len(x_list) * 100)

#Exercise 6A(v)

max_list = [max(collatzseq(i)) for i in x_list]
plt.xlabel("n")
plt.ylabel("max(n)")
plt.ylim(0, 100000)
plt.scatter(x_list, max_list, marker=".")
plt.loglog(x_list, max_list)
plt.semilogx(x_list, max_list)
plt.semilogy(x_list, max_list)
plt.show()

print([i for i in max_list if i > 25000])
print([i for i in x_list if (max(collatzseq(i)) > 25000)])

# On the standard plot we can see most values are small, with a few large outliers.
# The maximum is 250504 which occurs twice at n=703 and n=937. 937 is prime while 703=19*37.
# On the log log graph we can see that for each n, log(max(n)) cannot be smaller than n,
# so we see the line y=x. On the logy vs x graph we can clearly see a y=log(x) graph.



    
#Reminder: check your programme runs before submission! Your code should generate any figures when run. Do not upload/submit figures separately.