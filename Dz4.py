
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} їсть")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} гавкає ")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} нявкає ")

dog = Dog("Чіп", 3)
cat = Cat("Мілка", 2)

print("Собака:", dog.name, "Вік:", dog.age)
dog.eat()
dog.bark()

print("Кіт:", cat.name, "Вік:", cat.age)
cat.eat()
cat.meow()
