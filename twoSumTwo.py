def twoSumTwo(self, nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums) - 1

    while l < r:
        curSum = nums[l] + nums[r]
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return[l+1, r+1]
