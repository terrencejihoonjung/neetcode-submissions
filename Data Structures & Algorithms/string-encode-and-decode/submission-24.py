class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""

        ans = []
        for str in strs:
            ans.append(f"{len(str)}#{str}")
        return "".join(ans)

    def decode(self, s: str) -> List[str]:

        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length


            ans.append(s[start:end])
            i = end
        
        return ans
            



# solution 1: delimit by a non-valid ASCII character
# solution 2: add a character and the length of the string ("#5") before each string