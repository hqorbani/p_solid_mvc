def cover(func):
    def run_cover():
        print('before running')
        func()
        print('after running')
    return run_cover

@cover
def say_hello():
    print("hello")

say_hello()


