# https://www.acmicpc.net/problem/12759
# 2025-08-29 / 12759. 틱! 택! 토! / Silver V

# 하
# enumerate 변수 순서 반대로 적어서 틀렸었음

arr = [0] * 9
start = int(input())
for _n, i in enumerate(range(9), start):
    n = _n % 2 or 2
    y, x = map(lambda x: int(x) - 1, input().split())
    arr[y * 3 + x] = n

    idx = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (2, 4, 6),
        (0, 4, 8),
    ]
    if any(arr[a] > 0 and arr[a] == arr[b] == arr[c] for a, b, c in idx):
        print(n)
        break
else:
    print(0)
