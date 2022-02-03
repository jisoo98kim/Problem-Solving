# Link: https://leetcode.com/submissions/detail/633538250/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits)) # change to string
        change = int(''.join(digits)) + 1 # to combine as int + 1
        change_back = list(str(change)) # int -> str -> list
        result = list(map(int, change_back)) # target format
        return result
