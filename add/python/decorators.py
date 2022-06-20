def announce(f):
    def wrapper():
        print("i  want run the funtion ")
        f()
        print("Done with the funtion.")
    return wrapper


@announce
def hello():
    print('helo, world')

hello()