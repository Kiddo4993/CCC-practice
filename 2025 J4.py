import sys 

input = sys.stdin.readline 

N = int(input())

l = 0
firstp = 0

change = 0
maxstreak = 0

for r in range(N):
    letter = input().strip()

    if letter == "S":
        continue
    elif letter == "P":
        if change == 1:
            if maxstreak < (r  - l):
                maxstreak = (r - l)
            l = firstp + 1
            firstp = r

        elif change == 0:
            firstp = r
            change = 1

if maxstreak < (N -l):
    maxstreak = (N-l)

if change == 0:
    maxstreak = N - 1
            


print(maxstreak)