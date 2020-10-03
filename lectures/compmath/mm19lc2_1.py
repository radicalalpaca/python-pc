# Template file for Week 1

# Lines that start with '#' are comments and are ignored by Python.

#Exercise 1.A
#Write your answers in the line below the question number. Your answers should be enclosed in a print command, e.g. print(``6 September 1978'')

#A(i)
print("April 9")
#A(ii)
print("Friday")
#A(iii)
print("Sunday")
#A(iv)
print("Monday")

#Exercise 1.B
#Your answers should be enclosed in a print command, e.g. print(list(range(10))). Do not touch the lines of code defining a,b,x,y,
#but write your answers in the lines after them.

#B(i)
print([2 * i + 1 for i in range(50)])
#B(ii)
print([2 * i + 2 for i in range(50)])
#B(iii)
a = list(range(70,1030,3))
print(a[2])
#B(iv)
b = list(range(-41,10))
print(b[-2])
#B(v)
c = 10 * a + 5 * b
print(c[int(len(c) / 2)])
#B(vi)
x,y = [1,3,5],[2,4,6]
print(sum([x0 * y0 for x0, y0 in zip(x, y)]))
#B(vii)
print([x[1]*y[2] - x[2]*y[1],
       x[2]*y[0] - x[0]*y[2],
       x[0]*y[1] - x[1]*y[0]])
