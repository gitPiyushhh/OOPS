class Parent:
    def __init__(self):
        self.pub = 'Public'
        
        self._protect = 'Protect'
        
        self.__priv = 'Private'

class Child(Parent):
    def __init__(self):
        super().__init__()
    
    def access(self):
        print('Public is accessible: ', self.pub)
        print('Protected is accessible: ', self._protect)
        print('Private is not accessible: ', self.__priv)   ## // This throws an err {coz private members are permitted to be used within class itself}

c1 = Child()
c1.access()