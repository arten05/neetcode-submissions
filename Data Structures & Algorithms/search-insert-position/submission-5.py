class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r =  mid
        return r
        