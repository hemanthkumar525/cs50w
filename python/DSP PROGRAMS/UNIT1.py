class student():
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('All varialbe intialised')

    def show(self):
        print('Hello, my name is',self.name)
obj = student('Python')
obj.show()
