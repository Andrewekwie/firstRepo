import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    filemode="a",
    format=":%(levelname)s %(asctime)s - %(message)s"
    )
logging.info("server start")
class NameSurname:
    def __init__(self, name, surname):
        if(type(name) != str):
            raise TypeError(f"Name is not a string ")
        if(type(surname) != str):
            raise TypeError(f"Surname is not a string '{type(surname) }'")
        self.name = name
        self.surname = surname

class Student:
    student_amount = 0
    def __init__ (self,name, surname , age, height=160):
        self.ns = NameSurname(name, surname)
        self.age = age
        self.height = height
        Student.student_amount += 1

    def printStudent(self):
        print(f'Name: {self.ns.name}')
        print(f'Surname: {self.ns.surname}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')

    def Birthday(self):
        self.age += 1
        print(f'Happy Birthday to {self.ns.name}. Now you {self.age}!')


try:
    logging.debug("in proces")
    first_student = Student("andrew", "danu", 12)
    logging.info(f"info {first_student.ns.name} {first_student.ns.surname}")
except Exception as error:
    print(error)


print("Next code")
logging.info("server end")
#first_student.Birthday()