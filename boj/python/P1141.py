N = int(input())
words = [input() for _ in range(N)]
words.sort()
result = 0
for i in range(N):
    for w in words[i+1:]:
        if w.startswith(words[i]):
            break
    else:
        result += 1
print(result)
