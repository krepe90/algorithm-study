# https://www.acmicpc.net/contest/problem/1488/1

s = input()

if s[-1] in "aeiouns":
    # 모음으로 끝나는 단어나 n 또는 s로 끝나는 단어는 뒤에서 두 번째 모음에 강세를 준다.
    vowel = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] in "aeiou":
            if vowel:
                print(i + 1)
                exit()
            else:
                vowel += 1
else:
    # n, s 이외의 자음으로 끝나는 단어는 마지막 모음에 강세를 준다.
    for i in range(len(s) - 1, -1, -1):
        if s[i] in "aeiou":
            print(i + 1)
            exit()
print(-1)
