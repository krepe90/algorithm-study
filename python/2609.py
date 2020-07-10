# https://www.acmicpc.net/problem/2609
def gcd(a, b):
    # 최대공약수
    if a < b:
        a, b = b, a
    while b != 0:
        n = a % b
        a, b = b, n
    return a


N, M = map(int, input().split())
print(gcd(N, M))
print(N * M // gcd(N, M))
