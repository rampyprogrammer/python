from has import Heart
class Patient:
    def __init__(self,name,age,gender,beat):
        self.name=name
        self.age=age
        self.beat=beat
        self.gender=gender
        self.objH=Heart(self.name,self.beat)

    def details(self):
        print(f"""
                   name Of patient : {self.name}
                   age Of patient  : {self.age}
                   heart beat      : {self.beat}
                   Gender          : {self.gender}""")
objP=Patient("geeta",21,'female',75)
objP.details()
print('    Report  :')
objP.objH.evaluate()

