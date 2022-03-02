@staticmethod
def func1():
    """Some doc for staticmethod func"""
    print("Staticmethod func call")


@classmethod
def func2(self):
    """Some doc for classmethod func"""
    print("Classmethod func call")


class MyClass:
    method1 = func1
    method2 = func2


def call_func(func):
    try:
        func()
    except TypeError as err:
        print(f"TypeError: {err}")


def check_attrs(func):
    print("Attributes check:")
    try:
        print(f"{func.__name__=}")
    except AttributeError as err:
        print(f"AttributeError: {err}")
    try:
        print(f"{func.__doc__=}")
    except AttributeError as err:
        print(f"AttributeError: {err}")
    try:
        print(f"{func.__module__=}")
    except AttributeError as err:
        print(f"AttributeError: {err}")
    try:
        print(f"{func.__annotations__=}")
    except AttributeError as err:
        print(f"AttributeError: {err}")
    try:
        print(f"{func.__qualname__=}")
    except AttributeError as err:
        print(f"AttributeError: {err}")
    try:
        print(f"{func.__wrapped__=}")
    except AttributeError as err:
        print(f"AttributeError: {err}")


def main():
    call_func(func1) # A: regular function
    call_func(MyClass.method1) # B: class method
    call_func(MyClass().method1) # C: instance method
    call_func(func2) # A: regular function
    call_func(MyClass.method2) # B: class method
    call_func(MyClass().method2) # C: instance method

    check_attrs(func1)
    check_attrs(func2)


if __name__ == '__main__':
    main()