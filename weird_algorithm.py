n = int(input())
print(n, end="")
while n != 1:
    print(" ", end="")
    if n & 1:  # odd
        n = int(n * 3 + 1)
    else:
        n = int(n / 2)
    print(n, end="")
