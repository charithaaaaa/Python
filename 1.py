class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp_n={}
        for i in range (len(nums)):
            diff=target-nums[i]
            if diff in hp_n:
                return [hp_n[diff],i]
            hp_n[nums[i]]=i
#example
nums=list(map(int,input().split()))
target=int(input())
print(Solution().twoSum(nums,target))