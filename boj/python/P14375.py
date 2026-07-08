# https://www.acmicpc.net/problem/14375
# 2025-07-13 / 14375. The Last Word (Small) / Silver IV

# 브루트포스 하기, 3만개면 좀 많은데데 * 100
# 뭔가 줄일 수 있는게 있지 않을까?
# 그리디: 최대랑 같거나 크면 앞으로, 아니면 뒤로

T = int(input())
for i in range(1, T + 1):
    s = input()
    arr = [s[0]]
    mx = arr[0]
    for c in s[1:]:
        if c >= mx:
            arr.insert(0, c)
            mx = c
        else:
            arr.append(c)
    print("Case #{}: {}".format(i, "".join(arr)))
