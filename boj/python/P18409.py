# https://www.acmicpc.net/problem/18409
# 2026-02-22 / 18409. 母音を数える (Counting Vowels) / Bronze V

_ = input()
print(sum(1 for c in input() if c in "aeiou"))
