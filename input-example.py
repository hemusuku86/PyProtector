import datetime
import math

print("Hello, world!")
print(f"1 + 1 = {1 + 1}")
print(f"Today is {datetime.datetime.now()}")

number = int(input("enter a number > "))
if math.sqrt(number) % 1 == 0:
    print(f"{number} is a square number!")
else:
    print(f"{number} is not a square number...")

class obftest:
    def __init__(self, obf, test):
        self.a = f"{obf}{test}"
        self.data = {
            "here's true": True,
            2: [1,"a"],
            "your input": self.a
        }
        print(self.data)

obftest(test="test",obf="obfuscator")
