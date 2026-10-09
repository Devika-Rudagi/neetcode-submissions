class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26

        for i, j in zip(s, t):
           count[ord(i)-97] +=1
           count[ord(j)-97] -=1

        return all(x == 0 for x in count)