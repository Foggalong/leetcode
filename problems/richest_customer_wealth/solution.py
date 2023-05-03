class Solution:
    def maximumWealthForLoop(self, accounts: List[List[int]]) -> int:
        """
        Takes a matrix 'accounts' as input and returns the
        sum of the row entries which is greatest. Does this
        with a for loop.
        """

        # wealth is guaranteed to be at least 1
        max_wealth = 0

        # iterate over customers, find maximum wealth
        for customer in accounts:
            customer_wealth = sum(customer)
            if customer_wealth > max_wealth:
                max_wealth = customer_wealth

        # Python indexes from 0, customers from 1
        return max_wealth


    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Takes a matrix 'accounts' as input and returns the
        sum of the row entries which is greatest. Does this
        with a single line iterator comprehension.
        """
        return max((sum(customer) for customer in accounts))