
class NS:
    def __init__(self,name:str,surname:str):
        self.name = name
        self.surname = surname

class student:
    student_amount = 0
    def __init__ (self,name,surname,age,height=140,studing=False):
        self.ns = NS(name,surname)
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.studing = studing



    def printstudent(self):
        print(f"Name {self.ns.name}")
        print(f"surname {self.ns.surname}")
        print(f"age {self.age}")
        print(f"height {self.height}")
        if andrew.studing == None:
            andrew.studing = "not suding"
        else:
            andrew.studing = andrew.studing
        print(f"studing {self.studing}")

    def Birthday(self):
        print('happy Birthday')
        self.age +=1

print(f"before creating student {student.student_amount}")
andrew = student(str(input("name ")),str(input("surname ")),int(input("age ")),input("height "),input("studing (if not skip ) "))
print("")
print("")
andrew.printstudent()
andrew.Birthday()
print(f"after creating student {student.student_amount}")