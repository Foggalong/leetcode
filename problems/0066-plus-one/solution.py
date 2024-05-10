class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Given an integer represented as a list of digits, return
        a list of digits for the increment of that integer.
        """

        # work backwards through digits
        for i in range(len(digits)-1, -1, -1):
            # if 9, incremement and carry 1
            if digits[i] == 9:
                digits[i] = 0
            # otherwise, increment and done
            else:
                digits[i] += 1
                return digits
        # 1 carried beyond previous number of places
        return [1] + digits