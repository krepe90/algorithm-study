
n = int(input())
points = []
for i in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

T = int(input())
for _ in range(T):
    _ = input()
    cps = list(map(int, input().split()))
    td = 0
    for s, e in zip(cps[:-1], cps[1:]):
        d = ((points[s][0] - points[e][0]) ** 2 + (points[s][1] - points[e][1]) ** 2) ** 0.5
        td += d
    print(round(td))
