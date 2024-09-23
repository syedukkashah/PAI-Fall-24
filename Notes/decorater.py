def greet(fx):
    def mfx(): #wrapper function since it wraps around fx()
        print("PAI")
        fx()
        print("thanks")
    return mfx
@greet #shorthand for hello = greet(hello)
def hello():
    print("hello world")
hello()
