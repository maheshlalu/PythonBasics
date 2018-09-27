
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

#M
#method 1
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


#method 2


def findnegativeandpositivenumber(items):
    negativeList = list(filter(lambda x: x < 0, items))
    positiveList = list(filter(lambda x: x > 0, items))
    return (negativeList,positiveList)

numbersList = [1, 2, 3, 4, 5,-1,-4,-5]
print("negative number",findnegativeandpositivenumber(numbersList)[0])
print("positive number",findnegativeandpositivenumber(numbersList)[1])

#inverses

def inverseelement(elements):
    return elements[::-1]

print("inverse elements",inverseelement(numbersList))

#Sorting

def listsortingassendinganddesending(lst_sort):

    lst_sort.sort()
    print("The list  sort assending method:", lst_sort)

    lst_sort.sort(reverse=True)

    print("The list  sort desending method:", lst_sort)

print(listsortingassendinganddesending([9, 5, 7, 3, 1]))









