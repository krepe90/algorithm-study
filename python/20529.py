# B번 - 가장 가까운 세 사람의 심리적 거리
# https://www.acmicpc.net/contest/problem/578/2
# https://www.acmicpc.net/problem/20529
# Solved
# from sys import stdin
MBTI: dict = {"ISTJ": 0, "ISFJ": 1, "INFJ": 2, "INTJ": 3, "ISTP": 4, "ISFP": 5, "INFP": 6, "INTP": 7, "ESTP": 8, "ESFP": 9, "ENFP": 10, "ENTP": 11, "ESTJ": 12, "ESFJ": 13, "ENFJ": 14, "ENTJ": 15}
DIST: list = [
    [0, 1, 2, 1, 1, 2, 3, 2, 2, 3, 4, 3, 1, 2, 3, 2],
    [1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4, 2, 1, 2, 3],
    [2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3, 3, 2, 1, 2],
    [1, 2, 1, 0, 2, 3, 2, 1, 3, 4, 3, 2, 2, 3, 2, 1],
    [1, 2, 3, 2, 0, 1, 2, 1, 1, 2, 3, 2, 2, 3, 4, 3],
    [2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3, 3, 2, 3, 4],
    [3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2, 4, 3, 2, 3],
    [2, 3, 2, 1, 1, 2, 1, 0, 2, 3, 2, 1, 3, 4, 3, 2],
    [2, 3, 4, 3, 1, 2, 3, 2, 0, 1, 2, 1, 1, 2, 3, 2],
    [3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2, 2, 1, 2, 3],
    [4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1, 3, 2, 1, 2],
    [3, 4, 3, 2, 2, 3, 2, 1, 1, 2, 1, 0, 2, 3, 2, 1],
    [1, 2, 3, 2, 2, 3, 4, 3, 1, 2, 3, 2, 0, 1, 2, 1],
    [2, 1, 2, 3, 3, 2, 3, 4, 2, 1, 2, 3, 1, 0, 1, 2],
    [3, 2, 1, 2, 4, 3, 2, 3, 3, 2, 1, 2, 2, 1, 0, 1],
    [2, 3, 2, 1, 3, 4, 3, 2, 2, 3, 2, 1, 1, 2, 1, 0],
]
T: int = int(input())
for _ in range(T):
    # 1. 거리값은 0 (완전일치) 에서부터 4(완전히 다름)까지 될 수 있다.
    # 2. N의 값은 10만이 최대이나 실제로 고려해야할 연산의 개수는 48개
    N: int = int(input())
    A: list = input().split()
    # 2-1. 따라서 중복 제거
    cnt: list = [0 for n in range(16)]
    arr: list = []
    for m in A:
        if cnt[MBTI[m]] >= 3:
            continue
        else:
            cnt[MBTI[m]] += 1
            arr.append(MBTI[m])
    # 3. 불필요한 값이 제거된 arr에서 지옥의 3중반복문
    print(cnt)
    print(arr)
    min_val = 12
    for i in range(0, len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                print(f"{i} {j} {k}")
                _min = DIST[arr[i]][arr[j]] + DIST[arr[j]][arr[k]] + DIST[arr[i]][arr[k]]
                if _min < min_val:
                    min_val = _min
    print(min_val)
