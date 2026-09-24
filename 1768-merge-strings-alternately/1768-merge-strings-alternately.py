class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        
        # Alternate between word1 and word2
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
            
        # Append the remaining part of word1 (if any)
        if i < len(word1):
            result.append(word1[i:])
            
        # Append the remaining part of word2 (if any)
        if j < len(word2):
            result.append(word2[j:])
            
        return "".join(result)
