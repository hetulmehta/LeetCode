#  https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """o(n^2) solution
        sum=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i]==target:
                    return [i,j]
        """
    #    optimal sol O(n) using hashmap(dict in python)
        """ target=11
        n=[4,5,6]
        i=[0,1,2]
        m=[7,6,5]
        dic={7:0,6:1} condition satisfied for n=6,i=2
        """
        dic={}
        for i,n in enumerate(nums):
            m=target-n
            if n in dic:
                return([dic[n],i])
            else:
                dic[m]=i
                
            
                
            