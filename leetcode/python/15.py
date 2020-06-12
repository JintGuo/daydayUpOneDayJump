class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 双指针， 快排思路
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if tmp == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif tmp < 0:
                    left += 1 
                else:
                    right -= 1
        return res
        


    def threeSum_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 思路同上，遍历过程中不考虑去重，最后 set(res) 去重
        res = []
        if len(nums) < 3:
            return res
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if tmp == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif tmp < 0:
                    left += 1 
                else:
                    right -= 1
        return list(set(tuple(x) for x in res))        
        
