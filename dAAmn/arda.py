import pyfirmata2
import tkinter as tk

try:
    PORT = pyfirmata2.Arduino.AUTODETECT
except:
    print("Подключите вашу плату Arduino!")
root = tk.Tk()
root.title("trothle")
root.geometry("50x330")

board = pyfirmata2.Arduino(PORT)
pwm_5 = board.get_pin('d:5:p')
pwm_5.write(1)

def on_slider_change(val):
    try:

        pwm_value = (int(val) - 1) / 254  # Изменение диапазона от 1-128 до 0-1
        pwm_5.write(pwm_value)
        print(f"PWM Value: {pwm_value}")
    except Exception as e:
        print("Ошибка:", e)
def on_button1_click():
    pwm_5.write(1)
    try:
        slider.set(255)
    except:
        pass
def on_button3_click():
    pwm_5.write(0.7047244094488189)
    try:
        slider.set(200)
    except:
        pass



slider = tk.Scale(root, from_=1, to=180, orient=tk.VERTICAL, command=on_slider_change,length=255)
slider.pack(pady=5,side='top', anchor='nw')
slider.set(200)
button_frame = tk.Frame(root)
button_frame.pack(side='left', anchor='nw', padx=10)
button1 = tk.Button(root, text="shut up",command=on_button1_click)
button1.pack(pady=1, anchor='nw')
button2 = tk.Button(root, text="turn on",command=on_button3_click,)
button2.pack(pady=2, anchor='nw')

root.mainloop()
