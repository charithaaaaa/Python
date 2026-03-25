class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(1, len(nums)+1):
            if i not in nums:
                result.append(i)
        
        return result
#example    
nums=list(map(int,input().split()))
print(Solution().findDisappearedNumbers(nums))
