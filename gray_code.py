def gray(n):
    if n == 1:
        return ["0", "1"]
    else:
        a = gray(n - 1)
        return ["0" + t for t in a] + ["1" + t for t in reversed(a)]


print("\n".join(gray(int(input()))))
