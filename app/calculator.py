import math
import random

class Calculator:
    def __init__(self, first_arg, second_arg):
        self.first_arg = first_arg
        self.second_arg = second_arg

    def plus(self):
        return self.first_arg + self.second_arg

    def minus(self):
        return self.first_arg - self.second_arg

    def division(self):
        return self.first_arg / self.second_arg

    def multiplication(self):
        return self.first_arg * self.second_arg

    def degree(self):
        return math.pow(self.first_arg, self.second_arg)

    def arithmetic(self):
        return (self.first_arg + self.second_arg) * random.randint(2,20)
