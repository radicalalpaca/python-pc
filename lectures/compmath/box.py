def boxcounting(xlist,ylist,epsilon):

    from math import log

    # find min and max coordinates of the set
    xmin = min(xlist)
    xmax = max(xlist)
    ymin = min(ylist)
    ymax = max(ylist)

    # no. of boxes of side epsilon to cover whole set
    xcount = int((xmax-xmin)/epsilon)+1
    ycount = int((ymax-ymin)/epsilon)+1

    # initialise matrix of 0s, one entry per box
    check = [[0 for col in range(xcount)] for row in range(ycount)]

    # go through all points in set, if point in box ij, change matrix entry to 1
    for k in range(len(xlist)):
        i = int((xlist[k]-xmin)/epsilon)
        j = int((ylist[k]-ymin)/epsilon)
        check[j][i] = 1

    # count up all entries in matrix with entry 1
    boxcount=0
    for row in range(ycount):
        boxcount = boxcount+check[row].count(1)
    # return epsilon, N(epsilon), log(N)/log(1/epsilon)
    return log(1/epsilon),log(boxcount),log(boxcount)/log(1/epsilon)