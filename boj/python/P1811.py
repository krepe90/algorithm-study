while True:
    s = input()
    if s == "#":
        break

    target, guess = map(list, s.split())
    guess_str = "".join(guess)

    # black
    black = 0
    for i in range(len(guess)):
        if target[i] == guess[i]:
            black += 1
            target[i] = guess[i] = ""
    # grey
    grey = 0
    for i in range(len(guess)):
        if not guess[i]:
            continue
        if guess[i] == target[i - 1]:
            grey += 1
            target[i - 1] = guess[i] = ""
        elif i + 1 < len(guess) and guess[i] == target[i + 1]:
            grey += 1
            target[i + 1] = guess[i] = ""

    # white
    white = 0
    target_set = set(target)
    for i in range(len(guess)):
        if not guess[i]:
            continue
        if guess[i] in target_set:
            target_set.remove(guess[i])
            white += 1

    print(f"{guess_str}: {black} black, {grey} grey, {white} white")