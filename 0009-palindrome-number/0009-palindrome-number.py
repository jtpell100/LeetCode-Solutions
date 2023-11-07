class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        halfWord = int(len(word) // 2)
        for y in range(halfWord):
            if word[y] != word[len(word) - (y+1)]:
                return False
        return True