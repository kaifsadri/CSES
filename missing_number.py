n = int(input())  # line 1
S = n * (n + 1) / 2
M = sum(int(n) for n in input().split())
print(int(S - M))
