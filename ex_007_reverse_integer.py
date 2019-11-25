def reverse(x: int) -> int:
    r = int(str(x)[::-1]) if (x > 0) else -(int(str(x)[::-1].replace("-", "")))
    return 0 if (r > 2 ** 31 - 1) or (r < - 2 ** 31) else r