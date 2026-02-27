import datetime

print("Your Full Name")
print("Today's date:", datetime.date.today())

from utils import add, subtract

print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))

from utils import add, subtract, multiply

print("Multiplication:", multiply(5, 3))