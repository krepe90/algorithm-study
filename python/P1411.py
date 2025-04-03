import math

def normalize(s):
    char_map = {}
    result = []
    for c in s:
        if c not in char_map:
            char_map[c] = chr(len(char_map) + ord("a"))
        result.append(char_map[c])
    return "".join(result)

words = [normalize(input()) for _ in range(int(input()))]

count_map = {}
for w in words:
    if w not in count_map:
        count_map[w] = 0
    count_map[w] += 1

result = 0
for w, c in count_map.items():
    result += c * (c - 1) // 2
print(result)
