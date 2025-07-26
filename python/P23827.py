# https://www.acmicpc.net/problem/23827
# 2025-07-26 / 23827. 수열 (Easy) / Silver IV

N = int(input())
arr = list(map(int, input().split()))

dp = [0] * (N + 1)
for i in range(N)[::-1]:
    dp[i] = (dp[i + 1] + arr[i]) % 1_000_000_007

answer = 0
for i in range(N):
    answer = (answer + arr[i] * dp[i + 1]) % 1_000_000_007
print(answer)
