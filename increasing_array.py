n = int(input())  # line 1
l = list(int(n) for n in input().split())
res = 0
for ind in range(1, len(l)):
    if l[ind] < l[ind - 1]:
        res += l[ind - 1] - l[ind]
        l[ind] = l[ind - 1]
print(res)
