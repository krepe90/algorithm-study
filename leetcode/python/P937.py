# https://leetcode.com/problems/reorder-data-in-log-files/
# 2026-07-24 / 937. Reorder Data in Log Files (로그 파일 재정렬) / Medium


# 정렬조건:
# 1. 문자 로그 우선, 이어서 숫자 로그
# 2. 문자 로그는 사전순 정렬, 이어서 식별자로 정렬
# 3. 숫자 로그는 기존 정렬 순서 유지
# 내가 기억하기론 MZ한 파이썬부터는 정렬이 stable함을 보장하기 때문에 적당히 key 함수만 잘 만들어주면 될 것 같다

# 아니 " let1 art can" 에서 identifier가 "" 일 수가 있는건가?
# Each log is a space-delimited string of words, where the first word is the identifier.
# 라는데, 나는 len() == 0 인 string 을 'word' 라고 부를 수 있다는걸 오늘 처음 알았음
# 백준 부활좀


def k(s: str):
    print(s)
    i, w = s.split(sep=" ", maxsplit=1)
    if w[0].isdigit():
        return ("~",)
    return tuple((w, i))


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        logs.sort(key=k)
        return logs


if __name__ == "__main__":
    c = Solution()
    result = c.reorderLogFiles(
        logs=[
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ]
    )
    print(result)

    result = c.reorderLogFiles(
        logs=["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    )
    print(result)

    result = c.reorderLogFiles(
        logs=[
            "dig1 8 1 5 1",
            " let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ]
    )
    print(result)
