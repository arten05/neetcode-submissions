class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums) - 1
        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[r] == target:
            return r
        else:
            return -1




        