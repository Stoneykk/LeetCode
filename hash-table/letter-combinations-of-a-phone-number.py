class Solution:
    def __init__(self):
        self.LetterMap = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        ]
        
    def backtracking(self, digits, index, path, result):
        if index == len(digits):
            result.append(''.join(path))
            return
        digit = int(digits[index])
        letters = self.LetterMap[digit]
        for letter in letters:
            path.append(letter)
            self.backtracking(digits, index+1, path, result)
            path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) == 0:
            return result
        self.backtracking(digits, 0, [], result)
        return result