from collections import Counter

s = input()
L = ""
C = ""
T = Counter(s)
while T:
    t = T.popitem()
    if t[1] & 1:  # odd
        C = t[0] * t[1]
    else:
        L += t[0] * (t[1] // 2)
if len(L) + len(L) + len(C) == len(s):
    print(L, C, L[::-1], sep="")
else:
    print("NO SOLUTION")
