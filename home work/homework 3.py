import  logging
logging.basicConfig(level=logging.INFO,
                    filename="logs.log",
                    filemode="a", format="&(levelname)s:%(asctime)s - %(message)")
class NS:
    def __init__(self,name:str,surname:str):
        if(type(name)!= str):
            raise TypeError("name is not a string")
        if  (type(surname) != str):
            raise TypeError("surname is not a string")
        self.name = name
        self.surname = surname

class student:
    student_amount = 0
    def __init__ (self,name,surname,age,height=140,studing=False,grade = None):
        self.ns = NS(name,surname)
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.studing = studing
        self.grade = grade
        student.student_amount +=1
        logging.INFO(f"творення студента {self.ns.name},{self.ns.surname}")





    def printstudent(self):
        print(f"Name {self.ns.name}")
        print(f"surname {self.ns.surname}")
        print(f"age {self.age}")
        print(f"height {self.height}")

        if andrew.studing == "":
            andrew.studing = "not suding"
        else:
            if andrew.grade == 1 or andrew.grade == 2 or andrew.grade == 3:
                print("Grades: very bad")
            if andrew.grade == 4 or andrew.grade == 5 or andrew.grade == 6:
                print("Grades: bad")
            if andrew.grade == 7 or andrew.grade == 8 or andrew.grade == 9:
                print("Grades: Ok")
            if andrew.grade == 10 or andrew.grade == 11:
                print("Grades: good")
            if andrew.grade == 12:
                print("Grades: very good")
        print(f"studing {self.studing}")



    # def Birthday(self):
    #     print('happy Birthday')
    #     self.age +=1

print(f"before creating student {student.student_amount}")
try:

    andrew = student("andrew","danu",11 , 145, "yes")


    print(f"after creating student {student.student_amount}")



    if andrew.studing == "":
        pass
    else:
        andrew = student(grade=10, name=andrew.name, surname=andrew.surname, age=andrew.age, height=andrew.height,
                         studing=andrew.studing)

    print("")
    print("")
    andrew.printstudent()
    # andrew.Birthday()
except Exception as error:
    print(error)




