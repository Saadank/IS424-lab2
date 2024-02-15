def repeat_hello(repetitions):
    def decorator(func):
        def wrapper():
            for _ in range(repetitions):
                func()
        return wrapper
    return decorator

x = int(input("Enter a number of repetitions: "))

@repeat_hello(x)
def hello():
    print('Hello')
hello()
