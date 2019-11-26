def isPalindrome(x: int) -> bool:
    s = str(x)
    lght = len(s)
    for i in range(0, int(lght / 2)):
        if s[i] != s[lght - i - 1]: return False
    return True
