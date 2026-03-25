class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        nums[:]=nums[-k:]+nums[:-k]
#example
nums=list(map(int,input().split()))
k=int(input())
Solution().rotate(nums,k)
print(nums)