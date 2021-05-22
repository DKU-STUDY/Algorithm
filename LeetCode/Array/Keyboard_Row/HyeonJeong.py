class Solution(object):
    def findWords(self, words):
        alpha = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        for j, word in enumerate(words):
            word = list(set(word.lower()))
            for i, n in enumerate(alpha):
                if word[0] in n:
                    index = i
                    break
            state = 1
            for x in word[1:]:
                if x not in alpha[index]:
                    state = 0
                    break
            if state == 1:
                result += [words[j]]
        return result
