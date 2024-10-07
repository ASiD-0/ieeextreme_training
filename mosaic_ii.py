# numpy and scipy are available for use
import numpy
import scipy
from math import ceil
w = get_number()
h = get_number()
a = get_number()
b = get_number()
m = get_number()
c = get_number()

total_tiles = ceil(w/a)*ceil(h/b)
price = ceil(total_tiles/10)*m
worker_price = 0
if w % a != 0:
    worker_price += h*c
if h % b != 0:
    worker_price += w*c
total_price = worker_price + price
print(total_price)