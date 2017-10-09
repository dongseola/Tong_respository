def factorial(n) :                   #factorial code
    if (n==1) or (n==0) :
        return 1
    else :
        return factorial(n-1)*n

def return_factorial (number) :         #output and input-divide
    if  0 <= number :
        m = str(number)
        f = str(factorial(number))
        print ( m + "!" + " = " + f )
        m = int(input("Enter a number : "))
        input_number(m)
    elif number == -1 :
        pass
    else :
        print ("It can't")
        m = int(input("Enter a number : "))
        input_number(m)

def input_number(number):              #for make infinite
    return_factorial(number)

number = int(input("Enter a number : "))    #start
input_number(number)                        #input