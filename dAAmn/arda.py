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

        pwm_value = (int(val) - 1) / 254  # Изменение диапазона от 1-128 до 0-1
        pwm_5.write(pwm_value)
        print(f"PWM Value: {pwm_value}")
    except Exception as e:
        print("Ошибка:", e)


root = tk.Tk()
root.title("trothle")
root.geometry("300x150")


slider = tk.Scale(root, from_=1, to=200, orient=tk.VERTICAL, command=on_slider_change,length=2500)
slider.pack(pady=5)


root.mainloop()
