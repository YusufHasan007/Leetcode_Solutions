class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        out = []
        for i in nums:
            out.append(i*i)
        
        return sorted(out)
