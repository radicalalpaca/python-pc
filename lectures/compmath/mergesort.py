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
