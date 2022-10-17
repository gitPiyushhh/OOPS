# 1. Method Overloading {static polymorphism} --> By default not allowed in python
def fun(*args):
    
    for i in range(len(args)):
        pass ## // Do any operation here {Eg. add all arguments}

# 2. Method Overriding {dynamic polymorphism} --> Child inheriting method of parent with own modifications
class Parent:
    def fun(self):
        print('I am parent')

class Child(Parent):
    def fun(self):
        print('I am child')

c1 = Child()
c1.fun()