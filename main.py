import datetime
date = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day
ma = date - 2012
text = "youre age exacly like mine"
if month == 12 and day > 15:
        plusorminus = 0
else:
    plusorminus = 1
if plusorminus == 1:
    ma = date - 2013
else:
    ma = date - 2012
print(plusorminus)
print(month)
print(date)
print(ma)
a = int(input("your age - "))
n = input("your name - ")
if a > ma:
    yooy = a - ma
    text = "you are",yooy,"year older then me"
if a < ma:
    yooy = ma - a
    text = " you are", yooy, "younger then me "
pt = text
print("hello",n, text,"your age",a )
