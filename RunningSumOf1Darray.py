class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        count = 0
        l = []

        for i in range(len(nums)):
            count += nums[i]
            l.append(count)
            
        return l  
