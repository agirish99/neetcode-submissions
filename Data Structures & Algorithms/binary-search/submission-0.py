class Solution:
    def search(self, nums: List[int], target: int) -> int:   
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: # target is in the middle
                return mid

            elif nums[mid] < target:    # target on the right. Move left pointer
                left = mid + 1
            else: 
                right = mid - 1 # target on the left
        
        return -1
        