

n = 3  
m = 7
r = 3
c = 4
mosaic = [  [5, 2, 3, 0], # 5, 2, 3
            [2, 3, 1, 0], # 2, 3, 1
            [1, 2, 3, 0]] # 1, 2, 3 

v_shift= 0
h_shift = 0
r_mod = n % r
c_mod = m % c
print('the best solution')
v_min_sum = float('inf')
v_min_index = 0
for i in range(c):
    sub_array_sum = 0
    for k in range(r):
        result = [mosaic[k][(i + j) % c] for j in range(c_mod)]
        sub_array_sum += sum(result)
        print(result)
    if sub_array_sum < v_min_sum:
        v_min_sum = sub_array_sum
        v_min_index = i
    print(sub_array_sum)
    print('---')


v_min_sum = float('inf')
v_min_index = 0
for i in range(c):
    sub_array_sum = 0
    for k in range(r):
        result = [mosaic[k][(i + j) % c] for j in range(c_mod)]
        sub_array_sum += sum(result)
        print(result)
    if sub_array_sum < v_min_sum:
        v_min_sum = sub_array_sum
        v_min_index = i
    print(sub_array_sum)
    print('---')

