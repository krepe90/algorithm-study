# https://leetcode.com/problems/valid-palindrome/
# 2026-07-23 / 125. Valid Palindrome (유효한 팰린드롬) / Easy


# 정규표현식 [\d]는 [0-9] 가 아니라는 사실을 알게 되었다
# [\w] 도 A-Za-z 가 아니다
# 날먹하려던 자의 최후

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        return s == s[::-1]


if __name__ == "__main__":
    c = Solution()
    assert c.isPalindrome("A man, a plan, a canal: Panama") is True
    assert c.isPalindrome("race a car") is False
    assert c.isPalindrome(" ") is True
