class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False 
        n = len(nums)
        for i in range(n-1):
            for j in (i+1,n-1):
                if nums[i] == nums[j]:
                    flag = True
                    return flag
        return flag

        