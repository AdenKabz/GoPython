#working with classes and objects

class Person:
    #properties/variables/characteristics
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    #behavior/method/function
    def study(self):
        print("Student is studying")

#instantiating or creating an object

student1=Person("Hussein",23,"Male")
print(student1.name,student1.age,student1.gender)
student1.study()

student2=Person("Alex",45,"Male")
print(student2.name,student2.age,student2.gender)

student3=Person("Beatrice",34,"Female")
print(student3.name,student3.age,student3.gender)

