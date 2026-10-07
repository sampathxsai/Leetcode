class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        count = [0] * 26

        for word in words:
            for c in word:
                count[ord(c) - 97] += 1

        for x in count:
            if x % len(words) != 0:
                return False

        return True