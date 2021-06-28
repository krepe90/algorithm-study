# https://www.acmicpc.net/problem/2775
arr = [[n for n in range(1, 15)]]
for i in range(14):
    arr.append([sum(arr[i][:n]) for n in range(1, 15)])

for _ in range(int(input())):
    k, n = map(int, (input(), input()))
    print(arr[k][n - 1])
