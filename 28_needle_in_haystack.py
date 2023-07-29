# return the index of the first occurrence
class Solution:
    def strStr(self, haystack: str, needle: str):
        for i in range(len(haystack)-len(needle)+1):
            haystack_part = haystack[i:i+len(needle)]
            if haystack_part == needle:
                return i
        return -1