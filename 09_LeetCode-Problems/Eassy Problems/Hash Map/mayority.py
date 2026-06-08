class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mayority = {}
        max = 0
        for idx, n in enumerate(nums):
            mayority[n] = 1 + mayority.get(n,0)
            if mayority[n] > mayority[nums[max]]:
                max = idx
        return nums[max]