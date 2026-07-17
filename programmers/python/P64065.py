# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 2026-07-17 / 2019 카카오 개발자 겨울 인턴십 > 튜플 / Lv. 2
# <프로그래머스 코딩 테스트 문제 풀이 전략: 파이썬편> 4장. 문자열

# 이거 뭔가 functools 라이브러리의 reduce 같은거 써먹으면 충분히 날먹 할 수 있을 것 같은데

# 그리고 이 문제 2레벨인것도 문자 파싱때문인거같은데 이렇게 eval로 날먹해도 되는걸까 정규식써도 되겠지만

# 다른 사람 풀이 보니까 좀 더 깔끔하게 푸는 법이 있긴 했다
# 나의 경우는 일단 set을 만들고, 직전 set과의 차집합에 남는 딱 하나의 원소를 모아서 list로 만들었는데
# 그냥 많이 나온 숫자(원소) 순으로 정렬하면 됐던것
# 문제에 지시된 방법대로 푸는것도좋 좋지만, 조금 다른 시각으로 바라볼 수 있는 능력도 있으면 쪼금 더 좋을듯


def solution(s: str):
    arr = sorted(eval(f"[{s[1:-1]}]"), key=len)
    prev_set = set()
    answer = []
    for s in arr:
        answer.append((s - prev_set).pop())
        prev_set = s
    return answer


if __name__ == "__main__":
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print(solution("{{20,111},{111}}"))
    print(solution("{{123}}"))
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
