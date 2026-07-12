# https://school.programmers.co.kr/learn/courses/30/lessons/340198
# 2026-07-12 / PCCE 기출문제 > [PCCE 기출문제] 10번 / 공원 / Lv. 1

# DP로 풀면 될 것 같음
# 왼쪽 위에서부터 쭉 돌면서 그 전 3개가 비어있으면 +1, 아니면 1 (당연히 차있으면 0)

# 쪼금 너무 어렵게 풀려고 해서 3번이나 틀리는 사소한 이슈가 있었다
# 그와중에 문제 예제 이미지랑 예시 데이터랑 다른데?


def solution(mats: list[int], park: list[list[str]]):
    height = len(park)
    width = len(park[0])
    dp: list[list[int]] = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            c = park[y][x]
            if c != "-1":
                dp[y][x] = 0
            else:
                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1
    # print(*dp, sep="\n")
    max_square_size = max(max(a) for a in dp)
    placeable = [n for n in mats if n <= max_square_size]
    return max(placeable) if placeable else -1


if __name__ == "__main__":
    print(
        solution(
            [5, 3, 2],
            [
                ["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
                ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
            ],
        )
    )
