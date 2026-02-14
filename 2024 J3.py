N = int(input())

results = []
for _ in range(N):
    results.append(int(input()))

answer = set(results)

unique_scores = sorted(answer, reverse=True)

third = unique_scores[2]
count = results.count(third)

print(third, count)
