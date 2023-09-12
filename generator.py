s1="ballari institute of technolagy and management"
print(s1)
s2=""
for i in s1.split():
    s2+=i[::-1]+" "

#strip method is used to remove space around string
print(s2.strip())