class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Takes an integer n as input and then returns a list of strings
        where the ith element is "FizzBuzz" if i is divisible by 3 and 5,
        "Fizz" if i is divisible by 3, "Buzz" if i is divisible by 5,
        and i (as a string) otherwise.
        """

        # list of integer strings, with every 3rd and every 5th entry blank
        output = [str(i) if (i % 3 and i % 5) else "" for i in range(1,n+1)]
        # add Fizz to every 3rd entry
        for i in range(2, n, 3): output[i] += "Fizz"
        # add Buzz to every 5th entry 
        for i in range(4, n, 5): output[i] += "Buzz"

        return output
