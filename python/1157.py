w = input().upper()
d = {chr(n): 0 for n in range(65, 91)}
for c in w:
    d[c] += 1
ds = sorted(d.items(), key=lambda x: x[1], reverse=True)
if ds[0][1] == ds[1][1]:
    print("?")
else:
    print(ds[0][0])
