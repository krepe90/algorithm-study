# https://www.acmicpc.net/problem/31848
# 2025-07-29 / 31848. 엉성한 도토리 분류기 / Silver II

# 메모리 제한이 상당히 넉넉한걸 보니까 미리 계산하는게 맞는 것 같다.
# 구멍 하나 지날때마다 도토리 크기가 1씩 작아진다 == 구멍 크기가 1씩 커진다

# 이게 어떻게 이분탐색이지
# hole_list를 계단식으로 만들어서 이진탐색을 돌리면 되긴 하네
# 속보 이진탐색 구현방법 까먹음
# 1111144556667 <- 이렇게 있으면 x보다 큰 최초의 n을 찾는건데...


def bin_search(arr, n):
    left, right = 0, len(arr)
    while left < right:
        middle = (left + right) // 2
        if arr[middle] >= n:
            right = middle
        else:
            left = middle + 1
    return left + 1  # zero-based to one-based


N = int(input())
hole_list = [int(c) + i for i, c in enumerate(input().split())]
mx = 0
hole_list = [(mx := max(mx, n)) for n in hole_list]

Q = int(input())
dotories = map(int, input().split())  # not doritos

print(*(bin_search(hole_list, n) for n in dotories))
