# https://www.acmicpc.net/problem/1769
# 2025-08-28 / 1769. 3의 배수 / Silver V

s = input()
cnt = 0
while len(s) > 1:
    s = str(sum(map(int, s)))
    cnt += 1
print(cnt, "YES" if s in "369" else "NO", sep="\n")
