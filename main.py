from typing import List 
def twoSum(nums: List[int], target: int) -> List[int]: 

    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            if nums[i]+nums[j]==target:
                return [i, j]
    