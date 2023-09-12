from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

    def method3(self):
        print("my name is raam i am from bellary")

class B(A):
    def method1(self):
        print('hello i am going to be a python devloper')

    def method2(self):
        print("i want to see my self as skill full and experienced devloper after two years...")
obj=B()
obj.method3()
obj.method1()
obj.method2()