
#function def

# 0 1 1 2 3 5 8 13 21

#def functionName(pram,parm2.....):

def fabonicci(n):
    k = 0
    j = 1
    sub = 0
    list =[]
    for num in range(n):
        print(k)
        list.append(k)
        sub = k + j
        k = j
        j = sub
    return list
    #print(list)

#print(fabonicci(10))
#range(0,5) 0 1 2 3 4
k = fabonicci(9)
print("print k value",k)

def printname(list):
    posList = []
    negList = []
    for num in list:
        print(num)
        if num < 0 :
            negList.append(num)
        else:
            posList.append(num)
    return (posList,negList)

print(printname([1,2,3,4,-1]))

def inverseelement(list):
    print(list)

inverseelement([1,2,3])




