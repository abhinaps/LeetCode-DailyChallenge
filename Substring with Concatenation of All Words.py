from collections import Counter
def findSubstring(s, words):
        n = len(s)
        k = len(words)
        wordLength = len(words[0])
        substringSize = wordLength*k
        wordCount = Counter(words)
        
        def check(i):
            remaining = wordCount.copy()
            wordUsed = 0
            for j in range(i,i+substringSize,wordLength):
                sub = s[j : (j+wordLength)]
                if remaining[sub] > 0:
                    remaining[sub]  -= 1
                    wordUsed += 1
                else:
                    break
            return wordUsed == k
        res = []
        for i in range(n-substringSize+1):
            if check(i):
                res.append(i)
        
        return res