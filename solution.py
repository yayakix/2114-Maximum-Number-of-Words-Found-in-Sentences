class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for i in range(len(sentences)):
            if len(sentences[i].split()) > max:
                max = len(sentences[i].split())
        return max
