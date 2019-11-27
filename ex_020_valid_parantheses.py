def isValid(s: str) -> bool:
    dic = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    tempDic = []

    for i in range(len(s)):
        if s[i] in dic.keys():
            tempDic.append(s[i])
        elif not tempDic or s[i] != dic[tempDic.pop()]:
            return False
    return not len(tempDic)
