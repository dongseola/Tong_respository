import time

def fibo_iter(n) :
    fb = [0, 1]
    if n>2 :
        for i in range (1,n) :
            for j in range (i-1,i):
                fb.append(fb[j]+fb[i])
        return fb[-1]
    else :
        return fb[n]

def mmath(n,r):
    children = 1
    parent = 1
    for i in range(1,r+1) :
        children = children*n
        n = n-1
    for t in range(1,r+1) :
        parent = parent*r
        r = r-1
    return children/parent

def fibo_math(n) :
    answer = 0
    for i in range(1,n+1) :
        answer +=(mmath(n,i))*(((5**0.5)**(i))-((-(5**0.5))**i))
    return answer//((2**n)*(5**0.5))

def fibo_recu(n) :
    if n ==0 :
        return 0
    elif n==1 or n==2 :
        return 1
    else:
        return fibo_recu(n-1)+fibo_recu(n-2)


number = int(input("Enter number: "))
start_time = time.time()

print(fibo_iter(number))
first_time = time.time()

print(int(fibo_math(number)))
second_time = time.time()

print(fibo_recu(number))
third_time = time.time()

print(third_time-second_time)
print(second_time-first_time)
print(first_time-start_time)
