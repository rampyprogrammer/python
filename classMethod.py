class std:
    roll_no=1

    def ChangeRoll(cls):
        cls.roll_no+=1
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.roll_no=std.roll_no
    def details(self):
        print(f"""
                name   :{self.name}
                age    :{self.age}
                roll_no :{self.roll_no}""")

obj=std("sam",20)
obj.details()
print()

obj2=std("nagachytanya",24)
obj2.ChangeRoll()
obj2.details()

obj3=std("rama",23)
obj3.ChangeRoll()
obj3.details()
