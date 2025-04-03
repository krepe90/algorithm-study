

def calc_c(s):
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord("A")] += 1
    return cnt



T = int(input())
for _ in range(T):
    s = input()
    base = calc_c(s)
    W = int(input())
    for _ in range(W):
        w = input()
        cnt = calc_c(w)
        ans = 0
        for i in range(26):
            if base[i] < cnt[i]:
                print("NO")
                break
        else:
            print("YES")
