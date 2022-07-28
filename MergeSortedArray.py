class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in nums2:
            nums1.append(i)
            
            if len(nums2) == 0:
                return
            
            zero = 0
            if zero in nums1:
                nums1.remove(zero)
            
            nums1.sort()
