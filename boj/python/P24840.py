# https://www.acmicpc.net/problem/24840
# 2025-07-14 / 24840. Challenge Nine / Silver III

# 각 자리 수의 합이 9의 배수인 경우 조건이 성립
# 따라서 (맨 앞에 0을 넣는 경우를 제외하면)
# 0: 0, 9, 1: 8, ...
# 어디에 삽입해야 가장 작은 숫자가 될까?
# 삽입 대상 숫자 i가 가장 먼저 나오는 곳의 바로 뒤에 삽입하는게 맞다.

T = int(input())
for idx in range(1, T + 1):
    s = input()
    n_list = list(map(int, s))
    n_sum = sum(n_list)

    i = 9 - (n_sum % 9) if n_sum % 9 else 0

    for j in range(len(s)):
        if n_list[j] > i and (j or i):
            n_list.insert(j, i)
            break
    else:
        n_list.append(i)
    n_str = "".join(map(str, n_list))
    print(f"Case #{idx}: {n_str}")
