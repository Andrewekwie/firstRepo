import pyfirmata2
import tkinter as tk
try:
    PORT = pyfirmata2.Arduino.AUTODETECT
except:
    print("Подключите вашу плату Arduino!")


board = pyfirmata2.Arduino(PORT)
pwm_5 = board.get_pin('d:5:p')
pwm_5.write(0)

def on_slider_change(val):
    try:

        pwm_value = (int(val) - 1) / 127  # Изменение диапазона от 1-128 до 0-1
        pwm_5.write(pwm_value)
        print(f"PWM Value: {pwm_value}")
    except Exception as e:
        print("Ошибка:", e)


root = tk.Tk()
root.title("trothle")
root.geometry("300x150")


slider = tk.Scale(root, from_=1, to=128, orient=tk.HORIZONTAL, command=on_slider_change)
slider.pack(pady=20)


root.mainloop()
