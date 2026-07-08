# https://www.acmicpc.net/problem/32076
# 2025-06-24 / 32076. Easy as ABC / Silver IV

def is_adjacent(p1, p2):
    if p1 == p2:
        return False
    if abs(p1[0] - p2[0]) > 1 or abs(p1[1] - p2[1]) > 1:
        return False
    return True

def scan(d, p, *exclude) -> list:
    for c in "ABC":
        p_list = [n for n in d[c] if n not in exclude and is_adjacent(p, n)]
        if p_list:
            return p_list
    return []

def conv(g, *points) -> str:
    return "".join(g[p[0]][p[1]] for p in points)

G = [input() for _ in range(3)]
d = {"A": [], "B": [], "C": []}
for y in range(3):
    for x in range(3):
        d[G[y][x]].append((y, x))

if d["A"]:
    a = d["A"]
elif d["B"]:
    a = d["B"]
else:
    a = d["C"]

results = set()
for p1 in a:
    a2 = scan(d, p1)
    for p2 in a2:
        a3 = scan(d, p2, p1)
        results.update(conv(G, p1, p2, p3) for p3 in a3)
print(sorted(results)[0])

