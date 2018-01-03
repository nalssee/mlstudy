
# Manually downloaded the file 'housing.csv'
from sqlplus import *
import matplotlib.pyplot as plt


class Rets:
    def __init__(self, vals):
        self.vals = vals

    def hpr(self):
        result = 1
        for x in self.vals:
            result = result * (1 + x)
        return result

    def last(self):
        return self.vals[-1]

x = Rets([0.2, 0.3, -0.1])

print(x.hpr())



