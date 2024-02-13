s = input()
last = s[0]
rep = 0
result = 1
for ch in s:
    if ch == last:
        rep += 1
    else:
        last = ch
        result = max(result, rep)
        rep = 1
print(max(rep, result))
