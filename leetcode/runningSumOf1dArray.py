

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

    lp = 0
    rp = 1
    while(rp<len(nums)):
        sums = nums[lp] + nums[rp]
        nums[rp] = sums
        rp+=1
        lp = rp -1
        return nums