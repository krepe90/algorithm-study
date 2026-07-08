for _ in range(int(input())):
    M = int(input())
    p = 0
    m = 0
    for n in range(M):
        p1, p2 = map(int, input().split())
        m = m + p1 - p2
        p = min(m, p)
    print(-p)
