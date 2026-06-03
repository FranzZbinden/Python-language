class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupli = {}
        for n in nums:
            if n in dupli:
                return True
            else: 
                dupli[n] = True
        return False