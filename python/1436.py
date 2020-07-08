# https://www.acmicpc.net/problem/1436
# 상당히 느린편. 다른 해결방법은 없나
N = int(input())
cnt = 1
num = 666
while True:
    if cnt == N:
        break
    num += 1
    while "666" not in str(num):
        num += 1
    cnt += 1
print(num)
