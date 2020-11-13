import matplotlib.pyplot as plt
import random
import time

def mergesort(mylist):
    '''First we deal with lists of length 1 (or 0)'''
    if len(mylist) <= 1:
        return mylist

    '''We split longer lists into two halves, 
    and send each half to be sorted.'''
    m = len(mylist) // 2
    l = mergesort(mylist[:m])
    r = mergesort(mylist[m:])

    '''Finally we put the two sorted lists back together,
    interleaving them in the correct way.'''
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


def countingsort(mylist):
    n = max(mylist)
    bucket_list = (n + 1) * [0]
    for element in mylist:
        bucket_list[element] += 1
    return_list = []
    for i in range(n + 1):
        return_list.extend(bucket_list[i] * [i])
    return return_list


def timesortmethod(method):
    time_list = []
    for exponent in range(1, 21):
        unsorted_list = list(range(2 ** exponent))
        random.shuffle(unsorted_list)
        time_start = time.perf_counter()
        method(unsorted_list)
        sort_time_1 = time.perf_counter() - time_start
        time_list.append(sort_time_1)
    return time_list


x_list = [2 ** i for i in range(1, 21)]
plt.loglog(x_list, timesortmethod(sorted), label="tim sort")
plt.loglog(x_list, timesortmethod(countingsort), label="selection sort")
plt.ylabel("log(time)")
plt.xlabel("log(n)")
plt.legend()
plt.show()
