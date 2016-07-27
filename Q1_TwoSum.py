class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    	hashTable={}
    	for i, num in enumerate(nums):
    		if (target - num) in hashTable:
    			return [i, hashTable[target - num]]
    		hashTable[num] = i