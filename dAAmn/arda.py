import pyfirmata2
import tkinter as tk

# Автоматическое обнаружение порта и подключение к плате Arduino
try:
    PORT = pyfirmata2.Arduino.AUTODETECT
except:
    print("Подключите вашу плату Arduino!")

# Создаем объект платы
board = pyfirmata2.Arduino(PORT)
pwm_5 = board.get_pin('d:5:p')
pwm_5.write(0)

def on_slider_change(val):
    try:
        # Преобразование значения ползунка в диапазон 0-1 для PWM
        pwm_value = (int(val) - 1) / 127  # Изменение диапазона от 1-128 до 0-1
        pwm_5.write(pwm_value)
        print(f"PWM Value: {pwm_value}")
    except Exception as e:
        print("Ошибка:", e)

# Создаем главное окно
root = tk.Tk()
root.title("Пример с ползунком")
root.geometry("300x150")

# Создаем ползунок
slider = tk.Scale(root, from_=1, to=128, orient=tk.HORIZONTAL, command=on_slider_change)
slider.pack(pady=20)

# Запускаем главный цикл обработки событий
root.mainloop()
