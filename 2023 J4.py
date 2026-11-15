C = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

total = 0

for i in range(C):
    if arr1[i] == 1:
        total += 3
        if i > 0 and arr1[i - 1] == 1:
            total -= 2

    if arr2[i] == 1:
        total += 3
        if i > 0 and arr2[i - 1] == 1:
            total -= 2

    if arr1[i] == 1 and arr2[i] == 1 and i % 2 == 0:
        total -= 2

print(total)