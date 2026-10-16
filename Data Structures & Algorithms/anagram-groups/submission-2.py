class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = defaultdict(list)
        for st in strs:
            ch = [0] * 26
            for c in st:
                ch[ord(c)-ord('a')] += 1
            dicti[tuple(ch)].append(st)

        return list(dicti.values())
