# https://www.acmicpc.net/problem/13923
# 2025-07-22 / 13923. 오버워치 월드컵 / Silver III

# 조건은 "알파벳 종류는 n가지", "각 행·열에는 n가지 알파벳이 하나만 존재해야 함"
# 알파벳의 종류가 n+1개인 경우, n-1개인 경우 각각 생각해봐야 할 문제.

while True:
    try:
        n = int(input())
    except EOFError:
        break

    arr = [input() for _ in range(n)]

    data_all: dict[str, int] = {}
    data_row = [{} for _ in range(n)]
    data_col = [{} for _ in range(n)]

    # task 1. 갯수 세기
    for i in range(n):
        for j in range(n):
            c = arr[i][j]
            data_all[c] = data_all.get(c, 0) + 1
            data_row[i][c] = data_row[i].get(c, 0) + 1
            data_col[j][c] = data_col[j].get(c, 0) + 1

    # task 2. 이상 검출하기
    err = ans = "_"
    for k, v in data_all.items():
        if v == 1:
            err = k
        if v == n - 1:
            ans = k
    r, c = 0, 0
    for i, d in enumerate(data_row, 1):
        if len(d) != n or err in d:
            r = i
    for j, d in enumerate(data_col, 1):
        if len(d) != n or err in d:
            c = j

    print(r, c, ans)
