def romanToInt(s: str) -> int:
    result = 0
    dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for index in range(0, len(s)):
        if index > 0 and dic[s[index]] > dic[s[index - 1]]:
            result += dic[s[index]] - 2 * dic[s[index - 1]]
        else:
            result += dic[s[index]]
    return result
