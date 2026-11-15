import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

R = int(input_data[0])
C = int(input_data[1])
M = int(input_data[2])

prev_a = [0] * C
m = 0 

for row in range(R):
    curr_a = [0] * C
    
    for col in range(C):
        m += 1 
        if m > M:
            m = 1 
            
        if row == 0:
            curr_a[col] = m
            
        else: 
            if col == 0:
                min_cur = min(prev_a[0], prev_a[1])
                min_left = min_cur

            elif col < C - 1:
                min_right = min(prev_a[col], prev_a[col + 1])
                min_cur = min(min_left, min_right)
                min_left = min_right
                
            else:
                min_cur = min_left 

            curr_a[col] = min_cur + m 
            
    prev_a = curr_a

result = min(prev_a)
print(result)