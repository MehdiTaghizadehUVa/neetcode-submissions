class Solution:

    def encode(self, strs: List[str]) -> str:
        list_str = []
        for str_ in strs:
            len_str = str(len(str_)).zfill(3) + str_
            list_str.append(len_str)
            print(len_str)
        return "".join(list_str)


    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        ans = []
        while i < n:
            len_ = int(s[i:i+3])
            start = i + 3
            end = start + len_
            str_ = s[start:end]
            ans.append(str_)
            i = end

        return ans