list01=[43,4,5,5,6,7,87,80,44]

def findOven(num):
    return num%2==0

def findOverTen(num):
    return num>10

def inrangTenToFifty(num):
    return 10<=num<=50

def searchNumber(func_condition):
    for num in list01:
        if func_condition(num):
            yield num

ans=searchNumber(findOven)
for item in ans:
    print(item)

