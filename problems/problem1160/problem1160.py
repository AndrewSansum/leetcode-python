from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        score = 0
        for word in words:
            chars_copy = list(chars)
            for char in word:
                if char in chars_copy:
                    chars_copy.remove(char)
                else:
                    break
            else:
                score += len(word)
        return score
