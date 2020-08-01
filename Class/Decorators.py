def announce(f):
    def wrapper():
        print("Function about to run")
        f()
        print("Function running done")
    return wrapper
    
@announce
def hello():
    print("Hello World")
    
hello()