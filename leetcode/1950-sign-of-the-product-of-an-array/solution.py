class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        Given a list of integers (nums), return 1 if the product
        of those numbers is positive, -1 of if the product is
        negative, or 0 if it's zero.
        """       

        # count how many integers are negative
        negative_count = 0
        for number in nums:
            if number < 0:
                negative_count += 1
            elif number > 0:
                pass
            else:  # number == 0
                # if any zeros occur, product will be zero
                return 0
        
        # if negative_count odd, will be negative
        if negative_count % 2:
            return -1
        # if negative_count even, will be positive
        else:
            return 1

