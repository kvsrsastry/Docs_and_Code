from abc import ABC, abstractmethod
class Mammal(ABC):
    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def print_attr(self):
        print('Name : ' + self.name.center(20,'#'))
        print('Age : {a:^20}'.format(a=self.age))

class Human(Mammal):
    def __init__(self, name, age):
        super().__init__(name,age)
    
    def print_attr(self):
        #super().print_attr()
        Mammal.print_attr(self)
    
    def __str__(self):
        return '{}@@@{}'.format(self.age, self.name)

    def __len__(self):
        return len(self.name)

hum1 = Human('ganesh', 37)
print(type(hum1))
hum1.print_attr()
hum2 = Human('kvsr', 37)
hum2.print_attr()
print(isinstance(hum1,Human))
print(isinstance(hum2,Mammal))
print(issubclass(Human, Mammal))
print(hum1)
print(len(hum2))
