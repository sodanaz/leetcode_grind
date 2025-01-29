class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for char1, char2 in zip(word1, word2):
           result += char1 + char2
        if len(word1) > len(word2):
            result+= word1[-(len(word1)-len(word2)):]
        elif len(word1) < len(word2):
            result+= word2[-(len(word2)-len(word1)):]
        return result
        