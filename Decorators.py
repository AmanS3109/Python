def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")

    return wrapper


@announce  # decorator
def hello():
    print("Hello, world!")


hello()

# hello = announce(hello)  # hello is now a wrapper function(how we can use function normally)
# print(hello())

