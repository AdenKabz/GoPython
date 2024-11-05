#dealing with errors encountered

try: #used to check for an error
    print(number)

except: #helps to capture the error that has been identified in try block
    print("An error has occured")

#program to divide two numbers


try:
    num1=32
    num2=0
    print(num1/num2)
except:
    print("A zero division error occured")
finally: #gets executed whether there is an error or not
    peint("Success")
