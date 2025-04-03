# 홀수인 a에 대해서 (a & 0x01 == 1) a' + ''/0/1 + a, 단 a는 앞에 0을 포함할 수 있다.
# 문자열로 다룬 다음 변환하는게 성능상으로 좋진 않지만 그냥 뭐...

# 지금 생각해보니까 굳이 조합일 이유가 없구나... 바보였네

from itertools import product as p

a: set[int] = set((1, 3, 5, 7))
for i in range(1, 15):
    for j in p('01', repeat=i):
        s = ''.join(j) + '1'
        a.add(int(f"{s[::-1]}{s}", 2))
        a.add(int(f"{s[::-1]}0{s}", 2))
        a.add(int(f"{s[::-1]}1{s}", 2))
a_s = sorted(a)
print(a_s[int(input()) - 1])