from typing import List


def removeElement(nums: List[int], val: int) -> int:
    n = 0
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] == val:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    for i in range(len(nums)):
        if nums[i] != val:
            n += 1
    return n