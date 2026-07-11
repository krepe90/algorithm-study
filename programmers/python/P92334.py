# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 2026-07-11 / 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기 / Lv. 1

# 중복 신고는 1건으로 처리, 신고 횟수 제한 없음
# 각 id별로 신고한 회원 중 정지된 회원의 수를 반환
# 물론 정석대로라면 2차원 bool 배열을 만들어서 계산하는게 맞을 것 같긴 함.

# id: {id, ...} 인 내가 신고한 회원 목록
# id: {id, ...} 인 나를 신고한 회원 목록
# 을 각각 만든 다음, 나를 신고한 회원 목록의 길이가 k 이상인 것들만 모아서 정지 목록을 생성
# 이후 신고한 회원을 돌면서 정지목록 & 신고목록 해서 갯수를 출력

# n이 작지 않아서 좀 쫄렸는데 생각보다 실행시간이 엄청 적게 걸림


def solution(id_list: list[str], report: list[str], k: int):
    reports = {i: set() for i in id_list}
    reported = {i: set() for i in id_list}

    for r in report:
        a, b = r.split()
        reports[a].add(b)
        reported[b].add(a)

    banned = {i for i, d in reported.items() if len(d) >= k}
    answer = [len(reports[i] & banned) for i in id_list]
    return answer


if __name__ == "__main__":
    print(
        solution(
            ["muzi", "frodo", "apeach", "neo"],
            ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
            2,
        )
    )
    print(
        solution(
            ["con", "ryan"],
            ["ryan con", "ryan con", "ryan con", "ryan con"],
            3,
        )
    )
