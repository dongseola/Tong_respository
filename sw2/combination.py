def combin(n,r):
    if 0 <= r <= n:   #시간을 훨씬 줄일 수 있음
        if n == r or r == 0:
            return 1
        return combin(n-1,r-1) + combin(n-1,r)
    elif n == 0 and r > 0 :
        return 0
    else:
        return "Error"

def combin_other(n,r):
    children = 1
    parent = 1
    for i in range(1,r+1) :
        children = children*n
        n = n-1
    for t in range(1,r+1) :
        parent = parent*r
        r = r-1
    return children/parent


while True :            #반복으로 돌아가게 만들기
    try :
        num1 = int(input("Enter first number: "))
        if num1 >=0 :
            num2 = int(input("Enter second number: "))
            if num2 < 0 :               #num2 음수처리
                break
            else :
                print(combin(num1, num2))
                print(combin_other(num1,num2))
        else:                           #num1 음수처리
            break
    except ValueError:
        print("Please, enter number")
