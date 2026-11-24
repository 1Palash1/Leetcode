class Solution(object):
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def maxLength(self, nums):
        prod = 1
        if len(nums) == 2: return 2
        start, end = 0, 0
        n = len(nums)
        max_len = 2
        while end < n:
            if self.gcd(prod, nums[end]) == 1:
                prod *= nums[end]
                max_len = max(max_len, end - start + 1)
                end += 1
            else:
                prod /= nums[start]
                start += 1
        return max_len
        