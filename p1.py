def ind(l1,n):
    for i in range(len(l1)):
       if n==l1[i]:
          return i
       
    else:
      return "not found"


l1=[1,2,3,54,5,67]
n=int(input('eneter : '))
print(ind(l1,n))



