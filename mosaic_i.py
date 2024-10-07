# numpy and scipy are available for use
import numpy
import scipy
from math import ceil

total_baths = get_number()
black_cost = get_number()
pink_cost = get_number()


black_tiles = []
pink_tiles = []
for _ in range(total_baths):
    black_tiles.append(get_number())
    pink_tiles.append(get_number())

black_sum = sum(black_tiles)
pink_sum = sum(pink_tiles)

black_per_ten = ceil(black_sum/10)
pink_per_ten = ceil(pink_sum/10)

print(black_per_ten*black_cost + pink_per_ten*pink_cost)