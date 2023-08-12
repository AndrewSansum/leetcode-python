from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n < 1:
            raise ValueError

        ls = []
        for i in range(1, n + 1):
            string = ""
            if i % 3 == 0:
                string += "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            if not string:
                string = str(i)
            ls.append(string)
        return ls
