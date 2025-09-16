# https://www.acmicpc.net/problem/10709
# 2025-09-16 / 10709. 기상캐스터 / Silver V

H, W = map(int, input().split())
arr_i = [input() for _ in range(H)]
arr_o = [[0 if c == "c" else -1 for c in row] for row in arr_i]

for j in range(H):
    for i in range(1, W):
        if arr_o[j][i] == 0:
            continue
        if arr_o[j][i - 1] != -1:
            arr_o[j][i] = arr_o[j][i - 1] + 1
for r in arr_o:
    print(*r)
