#parent class
class Animal:
    #behavior
    def move(self):
        print("Animal is walking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")


#creating objects
a=Animal()

d=Dog()
d.move()
d.bark()
