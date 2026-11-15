import sys 
input = sys.stdin.readline 

from collections import deque
cost = 0

R = int(input().strip())
C = int(input().strip())

grid = [list(input().strip()) for i in range(R)]

A = int(input().strip())
B = int(input().strip())

def bfs(grid, start_row, start_col):
    global cost
    
    R , C = len(grid), len(grid[0])

    queue = deque([(start_row, start_col)])
    visited = {(start_row, start_col)}

    while queue: 
        row, col = queue.popleft()

        if grid[row][col] == "S":
            cost += 1
        elif grid[row][col] == "M":
            cost += 5
        elif grid[row][col] == "L":
            cost += 10

        for dr, dc in [(-1,0), (1,0), (0, -1), (0,1)]:
            new_row, new_col = row + dr, col + dc
        
            if (0 <= new_row < R and 
                0 <= new_col < C and
                grid[new_row][new_col] != "*" and  
                (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col))

bfs(grid, A, B)

print(cost)