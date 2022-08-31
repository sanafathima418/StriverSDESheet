# Time Complexity: O(N!) * O(N)
# Space Complexity: O(N) + O(N)

def findPermutations(s):
    
    permutations_list = []
    sub_list = []
    freq_map = [0] * len(s)
    
    def recur_permutation():
        if len(sub_list) == len(s):
            permutations_list.append("".join(sub_list))
            return 
        
        # For every element of string, check possibilities of using chars 
        # Loop throught possibilities at each step
        for i in range(len(s)):
            # If not in map, good to use for this step
            if not freq_map[i]:
                sub_list.append(s[i])  # Choose
                freq_map[i] = 1
                recur_permutation()  # Recurse for deeper layers(increase length of sub_list)
                sub_list.pop()        # Unchoose
                freq_map[i] = 0
        
    recur_permutation()
    return permutations_list
        
    
