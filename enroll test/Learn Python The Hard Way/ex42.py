
class Animal(object):
    pass

## Dog是一只Animal
class Dog(Animal):

    def __init__(self, name):
        ## 构造函数，设置name属性值
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        ## 构造函数，设置name属性值
        self.name = name

class Person(object):
    def __init__(self, name):
        ## 构造函数，设置name属性值
        self.name = name
        ## Person有一个pet
        self.pet = None

## Employee是一个Person
class Employee(Person):
    def __init__(self, name, salary):
        ## 继承基类的构造函数
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan


frank = Employee("Frank", 120000)

frank.pet = rover


flipper = Fish()

crouse = Salmon()

harry = Halibut()
