class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate, count = None, 0 
        candidate2, count2 = None, 0 

        for num in nums: 
            if num == candidate: 
                count += 1 
            elif num == candidate2: 
                count2 += 1 
            elif count == 0: 
                candidate, count = num, 1
            elif count2 == 0: 
                candidate2, count2 = num, 1
            else: 
                count -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for num in nums: 
            if num == candidate: 
                count1 += 1 
            elif num == candidate2:
                count2 += 1 
        
        res = []

        if count1 > len(nums) // 3: 
            res.append(candidate)
        if count2 > len(nums) // 3: 
            res.append(candidate2)
        
        return res
