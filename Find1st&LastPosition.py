class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
     
        c = []
    
        for i in range(len(nums)):
            if nums[i]==target:
                c.append(i)
                break
           
        for j in reversed(range(len(nums))):
            if nums[j]== target:
                c.append(j)
                break
        
        
        if len(c)>1:
            return c
        
        
        return [-1,-1]
        
