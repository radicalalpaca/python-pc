#Template for Week 8 Exercises

# import files here
import time
import random
import matplotlib.pyplot as plt

# Question 1 code
def selectionsort(mylist):
    sorted_list = []
    while len(mylist) > 0:
        lowest = mylist[0]
        for x in mylist:
            if x < lowest:
                lowest = x
        sorted_list.append(lowest)
        mylist.remove(lowest)
    return sorted_list

time_list_selectionsort = []
for exponent_1 in range(1, 11):
    unsorted_list_1 = list(range(2 ** exponent_1))
    random.shuffle(unsorted_list_1)
    time_start_1 = time.perf_counter()
    selectionsort(unsorted_list_1)
    sort_time_1 = time.perf_counter() - time_start_1
    time_list_selectionsort.append(sort_time_1)

# Question 2 code

x_list = [2 ** i for i in range(1, 11)]
plt.loglog(x_list, time_list_selectionsort, label="selection sort")
plt.ylabel("log(time)")
plt.xlabel("log(n)")


# Question 2 comment
# There is a straight line which implies that selection sort is O(n^k)
# for some k.


#Question 3 code for bubblesort:
def bubblesort(mylist):
    for i in range(len(mylist) - 1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    return mylist


# Question 4 code 

time_list_bubblesort = []
for exponent_2 in range(1, 11):
    unsorted_list_2 = list(range(2 ** exponent_2))
    random.shuffle(unsorted_list_2)
    time_start_2 = time.perf_counter()
    bubblesort(unsorted_list_2)
    sort_time_2 = time.perf_counter() - time_start_2
    time_list_bubblesort.append(sort_time_2)

plt.loglog(x_list, time_list_bubblesort, label="bubble sort")

#Question 5 code 
def mergesort(mylist):
    if len(mylist) <= 1:
        return mylist
    m = len(mylist) // 2
    l = mergesort(mylist[:m])
    r = mergesort(mylist[m:])
    result = []
    i = j = 0
    while len(result) < len(r) + len(l):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
        if i == len(l) or j == len(r):
            result.extend(l[i:] or r[j:])
            break
    return result
    
time_list_mergesort = []
for exponent_3 in range(1, 11):
    unsorted_list_3 = list(range(2 ** exponent_3))
    random.shuffle(unsorted_list_3)
    time_start_3 = time.perf_counter()
    mergesort(unsorted_list_3)
    sort_time_3 = time.perf_counter() - time_start_3
    time_list_mergesort.append(sort_time_3)

plt.loglog(x_list, time_list_mergesort, label="merge sort")
plt.legend()
plt.show()

    
#Question 5 comment
# The line has a smaller gradient than selection sort, which is O(n^2),
# so merge sort must be faster than O(n^2).
    
    
#Question 6 code


    
#Question 6 comment




#Question 7 code
#def countingsort(mylist):

    

#Question 8 code



#Question 8 comment




