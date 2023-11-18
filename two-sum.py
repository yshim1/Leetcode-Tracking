class Solution:
    def twoSum(self, nums, target):
        hm = {}
        for i , number in enumerate(nums):
            difference = target - number
            if difference in hm:
                return [i, hm[difference]]
            hm[number] = i