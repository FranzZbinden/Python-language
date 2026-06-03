class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i,word  in enumerate(strs):
            if len(prefix) > len(word):
                prefix = prefix[:len(word)]
            for index, letter in enumerate(word):
                try:
                    if prefix[index] != letter:
                        prefix = prefix[:index]
                except:
                    continue
            if prefix == "":
                return prefix
        return prefix
                