class Solution:
    def maxSubArraySum(self,arr,N):
        if not arr: return 0 
        
        #local and global max
        lmax = gmax = arr[0]
        
        for i in range(1, N): 
            if arr[i] > arr[i] + lmax: 
                lmax = arr[i]
            else: 
                lmax = lmax + arr[i]
            gmax = max(gmax, lmax)
        return gmax

import math 

def main(): 
  T= int(input())
  while(T > 0): 
    n = int(input())
    arr = [int(x) for x in input().strip().split()] 
    ob = Solution()
    print(ob.maxSubArraySum(arr,n)) 
    T -= 1
