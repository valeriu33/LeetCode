from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if nums is None: return 0
    j = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            j += 1
            nums.remove(nums[i])
    return j

