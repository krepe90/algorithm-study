# https://www.acmicpc.net/problem/31870
# 2025-08-05 / 31870. 버블버블 / Silver III

# 버블버블
# 버블소트...? 너무 비효율적이지 않나


def bubble(arr: list[int], op=int.__gt__):
    n = len(arr)
    cnt = 0
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if op(arr[j], arr[j + 1]):
                cnt += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return cnt


N = int(input())
A = list(map(int, input().split()))

asc = bubble(A.copy())
desc = bubble(A.copy(), int.__lt__) + 1

print(min(asc, desc))
