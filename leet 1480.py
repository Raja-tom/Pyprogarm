class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total=0
        a=[]
        for i in nums:
            total+=i  
            a.append(total)
        return a
obj=Solution()      
l=[1,2,3,4]  
print(obj.runningSum(l))