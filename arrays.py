#Arrays is a list that stores only similar data types

courses=["MIT","Cyber Security","Data Science"]
print(courses)

#Accessing an element in an array
print(courses[1])

#Looping through an element
for y in courses:
    print("Course is",y)

#Adding a new element
courses.append("Web Development")
print(courses)

#Adding an element while specifying position
courses.insert(1,"Public Administration")
print(courses)

#Adding more than obe element at the end
courses.extend(["Economics","Journalism"])
print(courses)

#Deleting an element
courses.remove("MIT")
print(courses)
