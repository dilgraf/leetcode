class Solution:
    def findTheDifference(self, s: str, t: str):
        #going through letters in the list
        for t_letter in list(t):
            #comparing number of the particular letter between two strings
            if list(s).count(t_letter) < list(t).count(t_letter):
                return t_letter