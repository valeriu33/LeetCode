from typing import List


def twoSum( nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        difference = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == difference:
                return [i, j]
