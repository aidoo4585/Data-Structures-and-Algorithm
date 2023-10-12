class Solution:
    def missingNumber(self, array, n):
        summation = n * (n+1) // 2
        total = sum(array)
        return summation - total

t = int(input())
for _ in range(0,t): 
  n = int(input())
  a = list(map(int, input().split())
  s = Solution().missingNumber(a,n)
  print(s)
