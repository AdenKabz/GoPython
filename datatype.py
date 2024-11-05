#data types in python

number=67 #integer
second=45.80 #float
greeting="Hello there" #String
isPythonInteresting=True #Boolean

print(number)
print(second)
print(greeting)
print(isPythonInteresting)

#Data Structures - Multiple values stored in a single variable

car=["toyota","nissan","vw"] #list -ordered and changeable
fruits=("mango","banana","apple") #turple -ordered but unchangeable
countries={"Kenya","Tunisia","Algeria"} #set -unordered and unchangeable
student={
    "firstname": "Jane",
    "age": 25,
    "course": "web development",
    "gender": "female"
    } #dictionary -key-value pair

print(car)
print(fruits)
print(countries)
print(student)
print(student["gender"])


#Determining a datatype

print(type(countries))
print(type(student))


#Typecasting -converting from one data type to another

print(float(number))
print(int(second))
