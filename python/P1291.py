# https://www.acmicpc.net/problem/1291
# 2025-09-01 / 1291. 이면수와 임현수 / Silver III

# 문제가 너무 개떡같다
# 이면수: 자릿수의 합이 홀수
# 임현수: 2, 4
#       또는 합성수 and 소인수 분해 시 소인수 갯수 짝수개


def f(n: int):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


s = input()
n = int(s)
prime_factors = f(n)
is_prime = len(f(n)) < 2

이면수 = n > 5 and sum(map(int, s)) % 2 == 1
임현수 = n in (2, 4) or (not is_prime and len(set(prime_factors)) % 2 == 0)

if 이면수 and 임현수:
    print(4)
elif 이면수:
    print(1)
elif 임현수:
    print(2)
else:
    print(3)
