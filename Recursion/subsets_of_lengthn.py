class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sub_list = []
        main_list = []
        n = 2  # subsets of length 2
        
        def backtrack(i):
            
            if len(sub_list) == n: # generating sub lits of length 2
                main_list.append(sub_list.copy())
                return 
            
            # Loop over combinations beyond current index
            # For generating non unique subsets of length 2 i.e, [3,3] then start below loop from 0 
            for j in range(i,len(nums)):
                sub_list.append(nums[j])
                backtrack(j+1)
                sub_list.pop()
            
        backtrack(0)
        return main_list
