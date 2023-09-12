def my_decorator(f):
    def inner_fun():
        print("i am the iron man")
        f()
        print("i will save the world")
    return inner_fun
@my_decorator
def fun():
    print("i am going to save the world")

# res=my_decorator(fun)
# res()
fun()

