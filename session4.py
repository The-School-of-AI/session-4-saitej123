import random
from decimal import *
import math
import inspect


class Qualean:
    def __init__(self, *args):

        self.number = random.choice([-1, 0, 1])
        self.value = round(self.number * (random.uniform(-1, 1)), 10)
        if self.number not in [-1, 0, 1, -1.0]:
            raise ValueError("input is not in [-1,0,1]")
        for arg in args:
            if arg == 0:
                self.number = 0
                self.value = 0
            if arg == 1:
                self.number = 1                
            if arg == -1.0:
                self.number = -1
            if arg not in [-1, 0, 1, -1.0]:
                raise ValueError("input is not in [-1,0,1]")

    def __repr__(self):
        return "Qualean Class Instance"

    def return_qualean(self):
        return self.value

    def __str__(self):
        return f"Qualean String for number: " + str(self.number)

    def __add__(self, other):
        if isinstance(other, Qualean):
            total = self.value + other.value
            return total
        if not isinstance(other, Qualean):
            return self.value + other
        else:
            raise ValueError

    def __eq__(self, other):
        if not isinstance(other, Qualean):
            return self.value + other == other + self.value
        return self.value == other.value

    def __float__(self):
        return float(self.value)

    def __ge__(self, value):
        return self.value >= value

    def __gt__(self, value):
        return self.value > value

    def __invertsign__(self):
        return -1 * self.value

    def __le__(self, value):
        return self.value <= value

    def __lt__(self, value):
        return self.value < value

    def __mul__(self, other):
        if isinstance(other, Qualean):
            sum = self.value * other.value
            return sum
        if not isinstance(other, Qualean):
            sum = self.value * other
            return sum
        else:
            raise ValueError

    def __bool__(self):
        return self.value != 0

    def __sqrt__(self):
        if self.value >= 0:
            return Decimal(math.sqrt(self.value))
        else:
            return str(round(math.sqrt(-1 * self.value), 10)) + "i"

    def get_item(self):
        return self.value

    def __and__(self, other):
        if isinstance(other, Qualean) and other.value:
            return bool(self.value and other.value)
        if not isinstance(other, Qualean) and other:
            return bool(self.value and other)
        else:
            return False

    def __or__(self, other):
        if isinstance(other, Qualean):
            return bool(self.value or other.value)
        if not isinstance(other, Qualean) and other:
            return bool(self.value or other)
        else:
            return True
