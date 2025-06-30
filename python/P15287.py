# https://www.acmicpc.net/problem/15287
# 2025-06-30 / 15287. Easy Quest / Silver IV

# 필요가 없더라도 유니콘한테 쓸데없는걸 받긴 해야 한다

n = int(input())
a = list(map(int, input().split()))

d = [0] * 1001
yuni = []

for a_i in a:
    if a_i < 0:
        if d[-a_i] > 0:
            d[-a_i] -= 1
        elif d[0] > 0:
            yuni.append(-a_i)
            d[0] -= 1
        else:
            print("No")
            break
    else:
        d[a_i] += 1
else:
    yuni.extend([1] * d[0])
    print("Yes")
    print(*yuni, sep=" ")
