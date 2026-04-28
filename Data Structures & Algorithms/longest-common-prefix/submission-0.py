class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0
        min_l = 201
        min_str = ""
        for string in strs:
            m = len(string)
            if m < min_l:
                min_str = string
                min_l = m
        
        for char in min_str:
            status = True
            for string in strs:
                if string[pointer] != char:
                    status = False
            if status:
                pointer +=1
                if pointer >= min_l:
                    break
        
        return min_str[:pointer]