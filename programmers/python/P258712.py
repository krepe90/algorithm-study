# https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 2026-07-10 / 2024 KAKAO WINTER INTERNSHIP > 가장 많이 받은 선물 / Lv. 1

# friends 로 2차원 배열(?)을 만들고 저장한 다음
# 각 친구별 선물 지수를 구하고
# 규칙에 따라 연산하면 된다 <- 이게 제일 귀찮은데요?
# 중복 연산의 비효율은 무시해도 될듯


def solution(friends: list[str], gifts: list[str]):
    # 1. 기본값 생성
    friends_count = len(friends)
    fmap = {name: i for i, name in enumerate(friends)}
    gift_graph = [[0] * friends_count for _ in range(friends_count)]
    for act in gifts:
        sender, receiver = act.split()
        gift_graph[fmap[sender]][fmap[receiver]] += 1

    # 2. 선물 지수
    _given = [sum(gift_graph[i]) for i in range(friends_count)]
    _taken = [
        sum(gift_graph[j][i] for j in range(friends_count))
        for i in range(friends_count)
    ]
    gift_index = [g - t for g, t in zip(_given, _taken)]

    # 계산
    max_gift = 0
    for i in range(friends_count):
        gift_count = 0
        for j in range(friends_count):
            if gift_graph[i][j] > gift_graph[j][i]:
                gift_count += 1
            elif gift_graph[i][j] == gift_graph[j][i]:
                if gift_index[i] > gift_index[j]:
                    gift_count += 1
        if max_gift < gift_count:
            max_gift = gift_count
    return max_gift


if __name__ == "__main__":
    print(
        solution(
            ["muzi", "ryan", "frodo", "neo"],
            [
                "muzi frodo",
                "muzi frodo",
                "ryan muzi",
                "ryan muzi",
                "ryan muzi",
                "frodo muzi",
                "frodo ryan",
                "neo muzi",
            ],
        )
    )
    print(
        solution(
            ["joy", "brad", "alessandro", "conan", "david"],
            [
                "alessandro brad",
                "alessandro joy",
                "alessandro conan",
                "david alessandro",
                "alessandro david",
            ],
        )
    )
    print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))
