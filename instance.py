class one:
    a=10
    def fun(self):
        print("i am instance method...")
        a=23
obj=one()
print(one.a)
obj.fun()
print(one.a)

