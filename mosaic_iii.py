n = 5 # Number of rows
m = 8  # Number of columns
r = 3  # Number of rows in mosaic
c = 4  # Number of columns in mosaic
mosaic = [[1,2,3,4],[5, 6, 7, 8],[9, 10, 11, 12]]

v_shift= 0
h_shift = 0
r_mod = n % r
c_mod = m % c

v_min_sum = float('inf')
v_min_indices = []
for shft in range(c):
    sum = 0
    for i in range(r):
        if isinstance(mosaic[0], list):
            for j in range(shft, shft+c_mod):
                sum += mosaic[i][j % c]
        else:
            for j in range(shft, shft+c_mod):
                sum += mosaic[j % c]
    if sum < v_min_sum:
        v_min_sum = sum
        v_min_indices = []
        v_min_indices.append(shft)
    elif sum == v_min_sum:
        v_min_indices.append(shft)

# print('index ', v_min_index,'sum',  v_min_sum)

h_min_sum = float('inf')
h_min_indices = []
for shft in range(r):
    sum2 = 0
    for i in range(shft, shft+r_mod):
        for j in range(c):
            sum2 += mosaic[i % r][j]
    
    if sum2 < h_min_sum:
        h_min_sum = sum2
        h_min_indices = []
        h_min_indices.append(shft)
    elif sum2 == h_min_sum:
        h_min_indices.append(shft)

# print('index ', h_min_index,'sum',  h_min_sum)

integer_width = m // c
integer_height = n // r
# print('integer_width', integer_width, 'integer_height', integer_height)


summ = 0
if isinstance(mosaic[0], list):  
    for sublist in mosaic:
        for item in sublist:
            summ += item
else:
    for item in mosaic:
        summ += item

total_sum_of_integer_mosaic = integer_height * integer_width  * summ

min_width_sum = integer_height * v_min_sum
min_height_sum = integer_width * h_min_sum

print(integer_width, integer_height)
print(v_min_sum, h_min_sum)
# print('min_width_sum', min_width_sum, 'min_height_sum', min_height_sum)

total_sum_of_integer_mosaic += min_width_sum + min_height_sum
print(min_height_sum)

# Initialize minimum values
min_sum = float('inf')  # Start with a large value
min_pair = (None, None)  # Initialize to None

# Iterate through all pairs of h_min_index and v_min_index
for h_index in h_min_indices:
    for v_index in v_min_indices:
        # Calculate the sum for the current pair
        current_sum = 0
        for i in range(r_mod):
            for j in range(c_mod):
                # Use modulo to ensure indices stay within bounds
                current_sum += mosaic[(h_index + i) % r][(v_index + j) % c]
        
        # Check if the current sum is less than the minimum found
        if current_sum < min_sum:
            min_sum = current_sum
            min_pair = (h_index, v_index)
total_sum_of_integer_mosaic += min_sum

# print('total_sum_of_integer_mosaic', total_sum_of_integer_mosaic)
print(total_sum_of_integer_mosaic)