# https://leetcode.com/problems/contains-duplicate/


def containsDuplicate(nums: list[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
