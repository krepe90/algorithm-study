# Solved
# https://www.acmicpc.net/problem/1004


# Solution 1
def check(po, pl):
    return (po[0] - int(pl[0])) ** 2 + (po[1] - int(pl[1])) ** 2 > int(pl[2]) ** 2


ret = []
for cnt in range(int(input())):
    po = 0
    p = input().split(" ")
    sp, ep = (int(p[0]), int(p[1])), (int(p[2]), int(p[3]))
    for pl in range(int(input())):
        i_pl = input().split(" ")
        c_sp, c_ep = check(sp, i_pl), check(ep, i_pl)
        if c_sp ^ c_ep:
            po += 1
    ret += [po]
for i in ret:
    print(i)
