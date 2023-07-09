class Solution:
  def twoSum(self, nums, target):
  
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
    dict_sum = {}
    if nums[i] in dict_sum:
        return [dict_sum[nums[i]], i]
    else
        dict_sum[target - nums[i]] = i
