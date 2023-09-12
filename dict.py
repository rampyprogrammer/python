l1=[10,20,30,40,20,40,50,30,10,50,60,70,10]
# d1={ele:l1.count(ele) for ele in set(l1)}
# print(d1)
d1={}
for i in set(l1):
    cnt=0
    for j in l1:
        if i==j:
            cnt+=1
    d1[i]=cnt
print(d1)
print(d1[10])
    