class Animal:
    def __init__(self,name,height,whidth,lenght,age):
        self.name = name
        self.height = height
        self.whidth = whidth
        self.lenght = lenght
        self.age = age

    def print_stats(self):
        print("")
        print(f"Name {self.name}")
        print(f"whidth {self.whidth}")
        print(f"height {self.height}")
        print(f"lenght {self.lenght}")
        print(f"age {self.age}")

cat_simon =Animal((input("name ")),(input("height ")),(input("whidth ")),input("lenght "),input("age "))
cat_simka =Animal("simka","8","6","50","2")

cat_simon.print_stats()
cat_simka.print_stats()