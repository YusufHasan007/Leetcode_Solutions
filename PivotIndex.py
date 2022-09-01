class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        arrSum = sum(nums) 
        rightsum = 0
        leftsum = 0
        
        for i in range(len(nums)):
            
            rightsum = arrSum - nums[i] - leftsum
            
            if rightsum == leftsum:
                return i
            
            leftsum += nums[i]
        return -1
