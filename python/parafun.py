def function1():
    print("hi I am function1")


def function2(func):
    print("Hi i am function 2 now i call function1")
    func()


function2(function1)
