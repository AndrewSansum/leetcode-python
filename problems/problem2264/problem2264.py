class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = None
        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] and num[i - 1] == num[i]:
                concatted = num[i - 2] + num[i - 1] + num[i]
                if result is None or int(concatted) > int(result):
                    result = concatted
        if result is None:
            result = ""
        return result
