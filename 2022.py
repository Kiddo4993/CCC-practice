n = int(input())
r, c = map(int, input().split())
arr = list(map(int, input().split()))
nums = [int(input()) for _ in range(3)]

R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

arr.append(x)
arr.pop()
len(arr)
arr.sort()

arr.sort()
arr.sort(reverse=True)
new_arr = sorted(arr)
pairs.sort(key=lambda x: x[1])

count = {}

for x in arr:
    count[x] = count.get(x, 0) + 1

for k, v in d.items():
    print(k, v)

if key in d:

s = set()
s.add(5)

arr = list(set(arr))

if x in s:

from collections import Counter

arr = [1,2,2,3,3,3]
c = Counter(arr)
print(c)

from collections import deque

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    q.append((nr, nc))

def dfs(r, c):
    visited[r][c] = True

    for dr, dc in dirs:
        nr, nc = r+dr, c+dc

        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and grid[nr][nc] != '#':
                dfs(nr, nc)

for r in range(R):
    for c in range(C):
        if not visited[r][c]:
            dfs(r, c)
            components += 1

from collections import defaultdict

d = defaultdict(int)

for x in arr:
    d[x] += 1

from collections import defaultdict

d = defaultdict(int)

for x in arr:
    d[x] += 1

d = defaultdict(int)
d["a"] += 1
