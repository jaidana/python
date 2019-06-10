for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals',x,'*', n//x)
            break
        else:
            print(n, 'is a prime number')

#another methode
for x in range(2,10):
    if x % 2 == 0:
        print("it's a not a prime number:", x)
        break
    else:
        print("that's a prime number:", x)
            
