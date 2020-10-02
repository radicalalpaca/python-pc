def fib(n):
    a = [1,2]
    sum = 0
    for i in range(n-2):
        a.append(a[i]+a[i+1])

    for i in range(n):
        if a[i] % 2 == 0 and a[i] < 4000000:
            sum += a[i]
        elif a[i] >= 4000000:
            break
            print(sum)
    print(sum)




    
        
        
        
