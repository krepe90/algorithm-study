# https://www.acmicpc.net/problem/32952
# 2026-02-15 / 32952. 비트코인 반감기 / Bronze II

# 초기 보상 R, 반감기 간격 K, 그리고 특정 블록의 번호 M
# r == 0 이 되는 이후 (무의미한 반복문 진행) 에 대한 탈출을 안걸어놔서 시간 초과 발생

R, K, M = map(int, input().split())
r = R
for n in range(0, M, K):
    if n < M < n + K:
        break
    r //= 2
    if r == 0:
        break
print(r)
