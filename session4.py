import random
from decimal import *
import math
import cmath
import inspect


class Qualean:
    def __init__(self, user_input):
        if user_input not in [-1, 0, 1]:
            raise ValueError("input is not in [-1,0,1]")
        else:
            self.user_choice = user_input
            self.value = round(user_input * (random.uniform(-1, 1)), 10)

    def __repr__(self):
        return "Qualean: {0}".format(self.user_choice)

    def return_qualean(self):
        return self.value

    def __str__(self):
        return f"Qualean String for number: " + str(self.user_choice)

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

    def __and__(self, other_object):
        if not bool(self.value):
            return False
        else:
            if isinstance(other_object, Qualean) and other_object.value:
                return bool(self.value and other_object.value)
            else:
                return False

    def __or__(self, other):
        if isinstance(other, Qualean):
            return bool(self.value or other.value)
        if not isinstance(other, Qualean) and other:
            return bool(self.value or other)
        else:
            return True
