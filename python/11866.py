# https://www.acmicpc.net/problem/11866
N, K = map(int, input().split())
A = list(range(1, N + 1))
result = list()
idx = 0
while A:
    idx += K - 1
    idx %= len(A)
    result.append(str(A.pop(idx)))
print(f"<{', '.join(result)}>")
