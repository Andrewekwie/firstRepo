
class NS:
    def __init__(self,name:str,surname:str):
        if(type(name)!= str):
            raise TypeError("nameis not a string")
        if  (type(surname) != str):
            raise TypeError("surname is not a string")
        self.name = name
        self.surname = surname

class student:
    student_amount = 0
    def __init__ (self,name,surname,age=...,height=160):
        self.ns = NS(name,surname)
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height



    def printstudent(self):
        print(f"Name {self.ns.name}")
        print(f"surname {self.ns.surname}")
        print(f"age {self.age}")
        print(f"height {self.height}")

    def Birthday(self):
        print('Birthday')
        self.age +=1

print(f"before creating student {student.student_amount}")
andrew = student(str(input("name ")),str(input("surname ")),int(input("age ")),input("height "))

print("")
print("")
andrew.printstudent()
andrew.Birthday()
print(f"after creating student {student.student_amount}")