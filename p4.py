def count_words():
    f=open("passwords.txt",'r')
    res=f.read()
    count=0
    for i in res.split():
        count+=1
    return count
print(count_words())



