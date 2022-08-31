# Time Complexity: O(N!) * O(N)
# Space Complexity: O(N) + O(N)

def findPermutations(s):
    s = list(s) # For simplicity in swapping
    
    permutations_list = []
    def recur_permutation(idx):
        if idx == len(s):
            # Base Case
            permutations_list.append(''.join(s))
            return 
      
        # Loop throught possibilities at each step from fixed index to end
        # For every element of string, swap fixed index with possibilities
        for i in range(idx,len(s)):
            s[idx],s[i] = s[i],s[idx]    # Swap
            recur_permutation(idx+1)  # Fix element at idx and check for possibilities of idx+1
            s[idx],s[i] = s[i],s[idx]    # Swap back
        
    recur_permutation(0)
    return permutations_list
        
    
