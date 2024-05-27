class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        diff = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff_ji = nums[j]-nums[i]
                diff.append(diff_ji)
        
        counter = 0
        for i in diff:
            if diff.count(i)>counter:
                counter = diff.count(i)
                num = i
        return counter+1