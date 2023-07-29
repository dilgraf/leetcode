class Solution:
    def repeatedSubstringPattern(self, s: str):
        n = len(s)
        substring = ""
        for i in range(n):
            substring += s[i]
            # operator * is used to repeat the substring n times
            #checking if the repeated substring x times is equal to the intial string
            if substring * (n//len(substring)) == s:
                if n//len(substring) == 1:
                    return False
                else:
                    return True
        return False