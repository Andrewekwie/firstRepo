import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs_animal.log",
    filemode="a",
    format="%(levelname)s %(asctime)s - %(message)s"
    )
logging.debug("in proces")
try:
    class Animal:
        logging.debug("in proces")
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
            logging.debug(f"added Animal {self.name} (whidth {self.whidth} height {self.height} lenght {self.lenght} age {self.age}) ")

    cat_simon =Animal("simon","10","8","90","8")
    cat_simka =Animal("simka","8","6","50","2")

    cat_simon.print_stats()
    cat_simka.print_stats()
except Exception:
    logging.error("EROOOR!!!!!!!!!")
