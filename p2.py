def bubble(List):
    for i in range(len(List)-1):
        for j in range(len(List)-i-1):
            if List[j]>List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
    



List=[8,94,5,4,34,2,1]
bubble(List)
print(List)