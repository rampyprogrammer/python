def check(l1,n):
    for i in range(len(l1)):
        if l1[i]==n:
            return i
    return 'not found!'



list=[1,2,34,5.6,60,2]
n=int(input("enter n :"))
print(check(list,n))