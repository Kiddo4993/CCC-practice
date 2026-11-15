from collections import defaultdict

N = int(input().strip())
freq = defaultdict(int)

for i in range(N):
    Z = input().strip()

    

    for i in range(len(Z)):
        if Z[i] == "Y":
            freq[i + 1] += 1
        else:
            freq[i + 1] += 0

value = max(freq.values())

bestdays = []

for k, v in freq.items():
    if v == value:
        bestdays.append(str(k))


print(",".join(bestdays))
