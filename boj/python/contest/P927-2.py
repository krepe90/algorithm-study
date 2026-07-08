import sys
fruits = {
    "STRAWBERRY": 0,
    "BANANA": 0,
    "LIME": 0,
    "PLUM": 0
}
for n in range(int(input())):
    s, x = sys.stdin.readline().strip().split()
    fruits[s] += int(x)
for fruit_name, fruit_cnt in fruits.items():
    if fruit_cnt == 5:
        print("YES")
        break
else:
    print("NO")
