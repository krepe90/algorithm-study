import sys
input = lambda: sys.stdin.readline().rstrip()
# print = sys.stdout.write

N = int(input())
xsum1, ysum1 = 0, 0
xsum2, ysum2 = 0, 0
for _ in range(N):
    x, y = map(int, input().split())
    xsum1 += x
    ysum1 += y
for _ in range(N):
    x, y = map(int, input().split())
    xsum2 += x
    ysum2 += y

print((xsum2 - xsum1) // N, (ysum2 - ysum1) // N)
