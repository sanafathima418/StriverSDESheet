class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
#         # Approach 1: Recursive Approach: TLE
#         # TC: O(3^N)
#         # SC: O(N) + O(N) + O(N)
        
#         def recur_frog(i, k):
#             # 1. Base Case
#             if i == len(stones) - 1:
#                 return True
            
#             # 2. Inductive Case
#             j = stones[i] + k - 1
#             if k > 1 and j in stones_dict and recur_frog(stones_dict[j], k - 1):
#                 return True
#             j += 1
#             if j in stones_dict and recur_frog(stones_dict[j], k):
#                 return True
#             j += 1
#             if j in stones_dict and recur_frog(stones_dict[j], k + 1):
#                 return True
            
#             return False
        
#         # Lookup dict
#         stones_dict = {x: i for i, x in enumerate(stones)}
#         if stones[1] != 1:
#             return False
        
#         # first step k=1 and start from index 1
#         return recur_frog(1, 1)
    
#         # Approach 2: DP Memoization
#         # TC: O(N^3)
#         # SC: O(N^2)
        
#         # Lookup dict
#         stones_dict = {x: i for i, x in enumerate(stones)}
#         dp_array = {}
        
#         def recur_frog(i, k):
#             # 1. Base Case
#             if i == len(stones) - 1:
#                 return True
            
#             # 2. Inductive Case
#             if k > 1 and (i,k) in dp_array:
#                 return dp_array[(i,k)]
            
#             j = stones[i] + k - 1
#             if k > 1 and j in stones_dict and recur_frog(stones_dict[j], k - 1):
#                 dp_array[(j,k-1)] = 1
#                 return True
#             j += 1
#             if j in stones_dict and recur_frog(stones_dict[j], k):
#                 dp_array[(j,k)] = 1
#                 return True
#             j += 1
#             if j in stones_dict and recur_frog(stones_dict[j], k + 1):
#                 dp_array[(j,k+1)] = 1
#                 return True
            
#             dp_array[(i,k)] = 0
#             return dp_array[(i,k)]
        
#         if stones[1] != 1:
#             return False
        
#         # first step k=1 and start from index 1
#         dp_array[(1,1)] = 1
#         return recur_frog(1, 1)

        # Approach 2: DP Tabulation - different from memoization (Pretty Hard)
        # TC: O(N^2) for going over all elements of array and their possible ks
        # SC: O(N^2) for dp array(stones_dict)
        
        # Lookup dict
        stones_dict = defaultdict(set)
        for i in range(len(stones)):
            stones_dict[stones[i]] = set()
            
        # 1. Base Case: stone:[list of possible k]
        stones_dict[0].add(0)
        
        # 2. Inductive Case
        # Iterate through all stones in the stones list.
        for i in range(len(stones)):
            
            # 2.1 Iterate through all possible jump sizes for the current stone.
            for k in stones_dict[stones[i]]:
                
                # 2.2 For each possible jump distance, try jumping with a jump distance k-1, k, k+1
                for step in range(k-1, k+2):
                    print(stones[i], step)
                    # 2.3 If step is valid then add k to the map
                    if step > 0 and stones[i]+step in stones_dict:
                        print("v")
                        stones_dict[stones[i]+step].add(step)
        
        print(stones_dict)
        return len(stones_dict[stones[-1]]) > 0

        