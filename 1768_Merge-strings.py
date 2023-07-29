class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        word1_list = list(word1)
        word2_list = list(word2)

        if len(word1_list) == len(word2_list):
            pass
        elif len(word1_list) > len(word2_list):
            while len(word2_list) < len(word1_list):
                word2_list.append('')
        elif len(word1_list) < len(word2_list):
            while len(word1_list) < len(word2_list):
                word1_list.append('')

        merged = [i1+i2 for i1, i2 in zip(word1_list, word2_list)]
        return ''.join(merged)