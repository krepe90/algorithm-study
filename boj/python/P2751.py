# https://www.acmicpc.net/problem/2751
# 솔직히 언어 기능으로 날로먹는듯;;
from sys import stdin
print("\n".join(map(str, sorted([int(stdin.readline()) for _ in range(int(input()))]))))
