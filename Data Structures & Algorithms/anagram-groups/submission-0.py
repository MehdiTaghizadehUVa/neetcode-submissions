class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            group = "".join(sorted(string))
            groups[group].append(string)
        
        return list(groups.values())