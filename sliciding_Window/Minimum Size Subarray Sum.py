class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        high=0
        low=0
        sum=0
        n=len(nums)
        ans=float('inf')

        for high in range(n):
            sum=sum+nums[high]

            while (sum>=target):
                length=high-low+1 
                ans=min(ans,length)
                sum=sum-nums[low]
                low=low+1

        if ans==float('inf'):
            return 0
        return ans
