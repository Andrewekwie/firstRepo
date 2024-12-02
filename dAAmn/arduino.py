import pyfirmata2
import time
import tkinter as tk










try:
    PORT = pyfirmata2.Arduino.AUTODETECT
except:
    print("conetc your arduino bozzo")



# Creates a new board
board = pyfirmata2.Arduino(PORT)
pwm_5 = board.get_pin('d:5:p')
pwm_5.write(0)


def on_button1_click():
    try:
        pwm_5.write(0)
    except:
        print("Eroor")
    print(pwm_5)

def on_button2_click():
    try:
        pwm_5.write(1)
    except:
        print("Eroor")
    print(pwm_5)


# Создаем главное окно
root = tk.Tk()
root.title("Пример с двумя кнопками")
root.geometry("300x150")

# Создаем первую кнопку
button1 = tk.Button(root, text="-10",command=on_button1_click)
button1.pack(pady=10)

# Создаем вторую кнопку
button2 = tk.Button(root, text="10", command=on_button2_click)
button2.pack(pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()