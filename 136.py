class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hp_n={}
        for i in nums:
            hp_n[i]=hp_n.get(i,0)+1
        for key,val in hp_n.items():
            if val == 1:
                return key
#example
nums=list(map(int,input().split()))
print(Solution().singleNumber(nums))