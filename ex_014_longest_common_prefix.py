from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs: return ""
    response = ""
    for charI in range(len(strs[0])):
        all_equal = True
        for wordI in range(len(strs) - 1):
            try:
                if strs[wordI][charI] != strs[wordI + 1][charI]:
                    all_equal = False
                    break
            except IndexError:
                all_equal = False
                break
        if not all_equal:
            break
        else:
            response += strs[0][charI]
    return response
