def rem(l1,n):
    for i in range(len(l1)):
        if l1[i]==n:
            l1=l1[:i]+l1[i+1:]
            break
    else:print( "ele not found !")
    exit()


l1=[1,2,3,4,6,7]
rem(l1,int(input("enter n:")))
print(l1)