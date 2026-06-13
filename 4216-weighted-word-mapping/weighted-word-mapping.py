class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        n = len(words)
        sumw = [0]*n
        for i in range(n):
            c = 0
            for j in words[i]:
                c+= weights[ord(j)-ord('a')]
            sumw[i]=c%26
        s=''
        for i in sumw:
            s+=chr(ord('z')-i)
        return s