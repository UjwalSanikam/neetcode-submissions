class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        visited = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    visited.append(words[i])
                    break
        return visited