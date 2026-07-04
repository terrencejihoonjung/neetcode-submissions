class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""

        ans = []
        for str in strs:
            ans.append(f"{len(str)}#{str}")
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        if s == "": return []

        ans = []
        i = 0
        while i < len(s):
            str_len = []
            while s[i].isdigit():
                str_len.append(s[i])
                i += 1
            str_len = int("".join(str_len))
            
            i += 1 # skip the "#" character

            ans.append(s[i:i + str_len])
            i += str_len
        
        return ans
            



# solution 1: delimit by a non-valid ASCII character
# solution 2: add a character and the length of the string ("#5") before each string