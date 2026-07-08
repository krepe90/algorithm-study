input()
it = map(int, input().split())
prev = next(it)
score = prev
for n in it:
    if n - prev > 1:
        score += n
    prev = n
print(score)
