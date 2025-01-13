class NumArray:
    def __init__(self, nums: List[int]):
        self.preSum = []
        self.preSum.append(0)
        for n in nums:
            self.preSum.append(n + self.preSum[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)