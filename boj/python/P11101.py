for _ in range(int(input())):
    s1 = [n.split(":") for n in input().split(",")]
    s2 = [n.split("&") for n in input().split("|")]
    t = {k: int(v) for k, v in s1}
    c = [max(t[c] for c in n) for n in s2]
    print(min(c))
