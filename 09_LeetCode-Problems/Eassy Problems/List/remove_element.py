class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        safe = 0

        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[safe] = nums[idx]
                safe += 1
        return safe