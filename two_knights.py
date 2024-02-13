def TwoKnights(n):
    if n == 1:
        return 0
    elif n == 2:
        return 6
    elif n == 3:
        return 28
    else:
        return (n**4 - 44 - 20 * (n - 3) - 28 * (n - 4) - 9 * (n - 4) * (n - 4)) // 2


n = int(input())
for k in range(1, n + 1):
    print(TwoKnights(k))
