class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        i = 0
        j = n - 1
        ans = [0] * n
        p = n - 1 if a >= 0 else 0

        while i <= j: 
            if a >= 0: 
                if self.quadratic(nums[i], a, b, c) >= self.quadratic(nums[j], a, b, c):
                    ans[p] = self.quadratic(nums[i], a, b, c)
                    i += 1
                else: 
                    ans[p] = self.quadratic(nums[j], a, b, c)
                    j -= 1
                p -= 1
            else: 
                if self.quadratic(nums[i], a, b, c) < self.quadratic(nums[j], a, b, c):
                    ans[p] = self.quadratic(nums[i], a, b, c)
                    i += 1
                else: 
                    ans[p] = self.quadratic(nums[j], a, b, c)
                    j -= 1
                p += 1
            
        return ans

    def quadratic(self, x, a, b, c):
        return a * x * x + b * x + c