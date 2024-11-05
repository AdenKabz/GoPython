#built-in library functions
y=max(76,56,34,52)
print(y)

x=min(75,43,27,68)
print(x)

z=pow(2,3)
print("The result is",z)

#user-defined functions: make use of def keyword to create a function

def greeting():
    print("Hello there!")
greeting() #calling a function

#function to get sum of two numbers
def add():
    num1=7
    num2=20
    print(num1+num2)
add()

#parameter and arguments: parameter is a variable and argument is the value

#function to multiply two numbers
def multiply(x,y):
    print(x*y)
multiply(12,56)
multiply(34,27)
multiply(87,9)

#function to display names of doctors
def doctor(name):
    print(name)
doctor("Steve")
doctor("Mary")
doctor("Frank")

