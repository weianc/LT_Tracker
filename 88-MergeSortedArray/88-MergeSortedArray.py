class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        p = len(nums1)-1

        if m == 0 and n == 0: 
            return
        elif m > 0 and n == 0: 
            nums1[0:i+1] = nums1[0:i+1]
        elif n > 0 and m == 0: 
            nums1[0:j+1] = nums2[0:j+1]

        
        while i >= 0 and j >= 0: 
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
                p -= 1
            elif j >= 0 and nums1[i] < nums2[j]:
                nums1[p] = nums2[j]
                j -= 1
                p -= 1
        
        # if i < 0 or j < 0
        if i >= 0: 
            nums1[0:p+1] = nums1[0:i+1]
        
        if j >= 0: 
            nums1[0:p+1] = nums2[0:j+1]
        