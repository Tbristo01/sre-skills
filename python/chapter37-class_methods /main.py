# class method - this allows operations realted to the class itself
# its take the class and the first parameter ,which represent the class itself .

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of Students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls == 0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count}"


student1 = Student("Tishaun", 4.0)
student2 = Student("James", 3.0)
student3 = Student("Bond", 2.5)
