def fun(*arg,**karg):
    print("positional arguments :")
    #variable argus
    for i in arg:
        print(i)
    print("key word argu's  :")
    for key,val in karg.items():
        print(key,val)

fun(1,2,3,name="jhone",age=32,gender='male')


