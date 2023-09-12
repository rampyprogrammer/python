def count_whitesp(s):
    count=0
    for i in s:
        
        if i==" ":
            count+=1
    return count
s='my name is rama'
print(count_whitesp(s))