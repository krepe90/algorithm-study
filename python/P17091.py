# https://www.acmicpc.net/problem/17091
# 2025-06-29 / 17091. 단어 시계 / Silver V

wh = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
]
w = [
    "",
    "one minute",
    "two minutes",
    "three minutes",
    "four minutes",
    "five minutes",
    "six minutes",
    "seven minutes",
    "eight minutes",
    "nine minutes",
    "ten minutes",
    "eleven minutes",
    "twelve minutes",
    "thirteen minutes",
    "fourteen minutes",
    "quarter",
    "sixteen minutes",
    "seventeen minutes",
    "eighteen minutes",
    "nineteen minutes",
    "twenty minutes",
    "twenty one minutes",
    "twenty two minutes",
    "twenty three minutes",
    "twenty four minutes",
    "twenty five minutes",
    "twenty six minutes",
    "twenty seven minutes",
    "twenty eight minutes",
    "twenty nine minutes",
    "half",
]

h = int(input())
m = int(input())

if m == 0:
    print(f"{wh[h]} o' clock")
elif 1 <= m <= 30:
    print(f"{w[m]} past {wh[h]}")
else:
    h = h + 1 if h < 12 else 1
    m = 60 - m
    print(f"{w[m]} to {wh[h]}")
