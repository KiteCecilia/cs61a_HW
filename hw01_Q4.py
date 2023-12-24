def hailstone(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        print(int(n))
        return 1 + hailstone(n // 2)
    else:
        print(int(n))
        return 1 + hailstone(3 * n + 1)