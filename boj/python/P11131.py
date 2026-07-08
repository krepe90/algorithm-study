for _ in range(int(input())):
    _ = input()
    n = sum(map(int, input().split()))
    if n == 0:
        print("Equilibrium")
    elif n > 0:
        print("Right")
    else:
        print("Left")
