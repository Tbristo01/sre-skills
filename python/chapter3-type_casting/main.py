# Typecasting = the process of converting a variable from one data type to another
#               str(), int() ,float(), bool()


name = "Tishaun Bristol"
age = 34
gpa = 3.2
is_student = True

# type()  - use to get the data type of a variable 

result= type(name)
print(result)

result= type(age)
print(result)

result= type(gpa)
print(result)

result= type(is_student)
print(result)


# converting float to int 

result = int(gpa)
print(type(result),result)


# convert a string to boolean 
name = bool(name)

print(name)