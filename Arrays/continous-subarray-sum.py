class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_dict = {0: -1}
        curr_sum = 0 

        for i in range(len(nums)): 
            curr_sum += nums[i]
            mod = curr_sum % k

            if mod in mod_dict: 
                if i - mod_dict[mod] >= 2: 
                    return True
            else: mod_dict[mod] = i
        return False

nums = [23,2,4,6,7]
k = 6 

subarray = Solution()
res = subarray.checkSubarraySum(nums, k)
