'''class student:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def avg(self):
        return (self.a + self.b)/2
    
s1 = student(10, 20)
print(s1.avg())


class student:
    name='Student'
    def __init__(self, a, b):
        self.a=a
        self.b=b

    @classmethod
    def info(cls):
        return cls.name
print(student.info())'''