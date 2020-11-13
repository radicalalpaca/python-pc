# Template for Week 8 Exercises

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


def timesortmethod(method):
    time_list = []
    for exponent in range(1, 11):
        unsorted_list = list(range(2 ** exponent))
        random.shuffle(unsorted_list)
        time_start = time.perf_counter()
        method(unsorted_list)
        sort_time_1 = time.perf_counter() - time_start
        time_list.append(sort_time_1)
    return time_list


# Question 2 code
x_list = [2 ** i for i in range(1, 11)]
plt.loglog(x_list, timesortmethod(selectionsort), label="selection sort")
plt.ylabel("log(time)")
plt.xlabel("log(n)")


# Question 2 comment
# There is a straight line which implies that selection sort is O(n^k)
# for some k.


# Question 3 code for bubblesort:
def bubblesort(mylist):
    for i in range(len(mylist) - 1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    return mylist


# Question 4 code
plt.loglog(x_list, timesortmethod(bubblesort), label="bubble sort")


# Question 5 code
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


plt.loglog(x_list, timesortmethod(mergesort), label="merge sort")


# Question 5 comment
# The line has a smaller gradient than selection sort, which is O(n^2),
# so merge sort must be faster than O(n^2).


# Question 6 code
plt.loglog(x_list, timesortmethod(sorted), label="timsort")


# Question 6 comment
# We can see on the graph that timsort is much faster than merge sort.


# Question 7 code
def countingsort(mylist):
    n = max(mylist)
    bucket_list = (n + 1) * [0]
    for element in mylist:
        bucket_list[element] += 1
    return_list = []
    for i in range(n + 1):
        return_list.extend(bucket_list[i] * [i])
    return return_list


# Question 8 code
plt.loglog(x_list, timesortmethod(countingsort), label="counting sort")
plt.legend()
plt.show()

# Question 8 comment
# Counting sort is more efficient than selection sort, bubble sort and merge sort,
# but less efficient than timsort. Counting sort is most efficient when the range
# of the list is small. For example, the list [5, 2, 0, 3, 4, 1] would solve quickly
# as the range is comparable to the length of the list. However the list
# [0, 1000, 4, 523, 41, 67, 295, 739, 124, 598] would solve slower as the range is
# greater than the cube of the length, so the time complexity would be O(n^3).
