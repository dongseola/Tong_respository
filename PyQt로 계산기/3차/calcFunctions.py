from math import factorial as fact

def factorial(numStr):
    try:
        n = int(eval(numStr))
        r = str(fact(n))
    except:
        r = 'Error!'
    return r



def decToBin(numStr):
    try:
        n = int(eval(numStr))
        r = bin(n)[:]
    except Exception as e:
        print(e)

        r = 'Error!'
    return r



def binToDec(numStr):
    # try:
    #     n = eval(numStr)
    #     n = int(numStr, 2)
    #     r = str(n)
    # except:
    #     r = 'Error!'
    # return r
    return str(eval(numStr))


romans = [
    (100,'M'),(900, 'CM'),(500, 'D'),(400,'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40,'XL'),
    (10, 'X'), (9,'IX'), (5,'V'), (4,'IV'),
    (1,'I')]

def decToRoman(numStr):
    try :
        result = ''
        n= int(eval(numStr))

        if n >= 4000 :
            return 'Error!'

        for value, letter in romans:
            while n>=value:
                result+= letter
                n -= value
    except :
        result = "Error!"
    return result




def romanToDec(numStr):
    try :
        n= str(numStr)
        result = 0

        for number, roman in romans:
            while n != '':
                if n[0:2] == roman:
                    result+= number
                    m = n[2:]
                    n = m
                elif n[0] == roman :
                    result += number
                    m = n[1:]
                    n = m
                else :
                    break

    except :
        result = "Error!"
    return result