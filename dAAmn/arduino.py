import pyfirmata2
import time
try:
    PORT = pyfirmata2.Arduino.AUTODETECT
except:
    print("conetc your arduino bozzo")

answer = input("T or F ")


# Creates a new board
board = pyfirmata2.Arduino(PORT)
pwm_5 = board.get_pin('d:5:p')
pwm_5.write(0)
if answer == "T":
    while True:
        pwm_5.write(0)
        time.sleep(0.2)
        pwm_5.write(1)
        time.sleep(0.2)
while True:
    try:
        pwm_5.write(int(input("SPEEEEED or not? (1-128)")))
    except:
            try:
                pwm_5.write(int(input("SPEEEEED or not? (1-128)")))
            except:
                print("stoopid")
