def remov_dup(inputList):
    uniqueList=[]
    for item in inputList:
        if item not in uniqueList:
            uniqueList.append(item)

    return uniqueList

inputList=[1,2,3,2,4,5,3,93,9,8,8]
print(remov_dup(inputList))