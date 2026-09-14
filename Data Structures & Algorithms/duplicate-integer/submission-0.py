class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d1 = len(set(nums))
        d2 = len(nums)

        if d1 == d2:
            return False

        return True
        