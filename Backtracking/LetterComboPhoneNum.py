class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        combo_dict = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        sub_list = []
        main_list = []
        
        def backtrack(i):
            
            if len(sub_list) == len(digits) : 
                main_list.append("".join(sub_list))
                return 
            
            possibilities = combo_dict[int(digits[i])]
            for letter in possibilities:
                sub_list.append(letter)
                backtrack(i+1)
                sub_list.pop()
        
        backtrack(0)
        return main_list