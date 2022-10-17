class Parent:
    def __init__(self):
        print('I am Parent')

class Child(Parent):
    def __init__(self): 
        super().__init__()  ## // Super is used to access the parent methods 
    

c1 = Child()