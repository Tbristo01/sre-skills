# class variables =  shared amounts all instance of the call
# defined outside of the constructor
# Allows you to share data amongs all objects created from that class

class Students:
    class_year = 2024
    number_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.number_of_students += 1


student1 = Students("Tishaun", 35)
student2 = Students("John", 30)
student3 = Students("Michael", 27)
student4 = Students("Josh", 26)


print(f"My graduating class of {Students.class_year} has {Students.number_of_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)