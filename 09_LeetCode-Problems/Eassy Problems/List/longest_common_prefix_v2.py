class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for w in strs:
            if len(w) < len(prefix):
                prefix = prefix[:len(w)]
            for idx,(l,r) in enumerate(zip(w,prefix)):
                if l != r:
                    prefix = prefix[:idx]
        return prefix
