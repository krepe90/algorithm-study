# https://leetcode.com/problems/reverse-string/
# 2026-07-24 / 344. Reverse String (문자열 뒤집기) / Easy


# 정석대로면 중간지점까지 양 끝에서 서로 바꾸는건데
# 그냥 .reverse() 메소드 쓰면 되는구나...


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]


if __name__ == "__main__":
    c = Solution()

    s = ["h", "e", "l", "l", "o"]
    c.reverseString(s)
    print(s)

    s = ["a", "b", "c", "d"]
    c.reverseString(s)
    print(s)

    s = ["H", "a", "n", "n", "a", "h"]
    c.reverseString(s)
    print(s)
