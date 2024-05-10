class Solution:
    """
    Given a sorted array of unique integers containing 1 and prime numbers
    and an integer k, return the two array elements which when divided
    produce the kth smallest value of all elements in the list.
    """

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        """Use the best of the attempt below for the solution"""
        return self.TotalEnumeration(arr, k)


    def TotalEnumeration(self, arr: List[int], k: int) -> List[int]:
        """
        Poor O(nlogn) solution, doesn't make use of `arr` being sorted. My
        initial attempt, took about 20ish minutes mostly spent trying to
        remember how to sort a dict by key value in Python 3.  Was only
        then that I noticed that the values to consider is reduced by the
        restriction 0 <= i < j < n, so got this after another 10 mins.

        Despite repeated attempts to make it more efficient, this was the
        only one which passed all the test cases within the time limit.
        """

        n = len(arr)
        # construct a dictionary of form {p1/p2: [p1, p2]}
        prime_fractions = {}

        # iterate only over the valid pairs of primes
        for i in range(0, n-1):
            for j in range(i+1, n):
                prime1, prime2 = arr[i], arr[j]
                prime_fractions[prime1/prime2] = [prime1, prime2]
        
        # sort dictionaty in ascending order by key value
        prime_fractions = sorted(prime_fractions.items())

        # prime_fractions now a list of tuples (p1/p2, [p1, p2])
        return prime_fractions[k-1][1]  # question indexes from one


    def StringEnumeration(self, arr: List[int], k: int) -> List[int]:
        """
        Cursed O(nlogn) solution. Follows the same structure as total
        enumeration, but to "save" memory rather than using a it uses
        a list of strings which it then evaluates when sorting. This
        unfortunately passes all the test cases, but takes too long.
        """

        n = len(arr)
        # construct a list of form ["p1/p2", ...]
        prime_fractions = []

        # iterate only over the valid pairs of primes
        for i in range(0, n-1):
            for j in range(i+1, n):
                prime_fractions.append(f"{arr[i]}/{arr[j]}")
        
        # sort dictionaty in ascending order by key value
        prime_fractions = sorted(prime_fractions, key=lambda x: eval(x))

        # fractions in form "p1/p2", so split to [p1, p2]
        return [int(i) for i in prime_fractions[k-1].split("/")]


    def ins2srt(self, array: List[int], p: int) -> (List[int], int):
        """
        Utility function which inserts an integer p into a sorted list of
        of integers array, preserving sorting. Returns the new list and
        the index where the insertion occured.
        """

        n = len(array)

        for i in range(n):
            if p < array[i]:
                array[i:i] = [p]
                return array, i

        # handles case where p is the new biggest element
        array.append(p)
        return array, n


    def TotalEnumerationSansSort(self, arr: List[int], k: int) -> List[int]:
        """
        Builds on the idea of "TotalEnumeration", but removes the need to
        sort the values at the end because it constructs a pair of linked
        arrays to preseve sorting. Came after another ~20 minutes work.
        Unfortunately this runs out of time after 44/59 test cases.
        """

        n = len(arr)
        fraction_value = []  # gives p_i/p_j
        fraction_pairs = []  # gives (p_i, p_j)

        # iterate only over the valid pairs of primes
        for i in range(0, n-1):
            for j in range(n-1, i, -1):
                p_i, p_j = arr[i], arr[j]
                fraction_value, l = self.ins2srt(fraction_value, p_i/p_j)
                fraction_pairs[l:l] = [[p_i, p_j]]

        # prime_fractions now a list of tuples (p1/p2, [p1, p2])
        return fraction_pairs[k-1]


    def TotalEnumerationMinStore(self, arr: List[int], k: int) -> List[int]:
        """
        Builds on the above, but removes the need to story any more than k
        value pairs at a given time. Unfortunately this runs out of time 
        after 46/59 test cases.
        """

        n = len(arr)
        fraction_value = []  # gives p_i/p_j
        fraction_pairs = []  # gives (p_i, p_j)
        fraction_found = 0   # length of lists above

        # iterate only over the valid pairs of primes
        for i in range(0, n-1):
            for j in range(n-1, i, -1):
                p_i, p_j = arr[i], arr[j]
                fract = p_i/p_j

                # consider only if lists have space or found k-smallest 
                if (fraction_found < k) or (fract < fraction_value[-1]):
                    fraction_value, l = self.ins2srt(fraction_value, p_i/p_j)
                    fraction_pairs[l:l] = [[p_i, p_j]]

                    # only store the k-smallest pairs
                    fraction_found += 1
                    if fraction_found > k:
                        fraction_value.pop(-1)
                        fraction_pairs.pop(-1)

        # prime_fractions now a list of tuples (p1/p2, [p1, p2])
        return fraction_pairs[-1]


    def PartialEnumeration(self, arr: List[int], k: int) -> List[int]:
        """
        As you can tell, this was ideally leading to a solution which only
        did partial enumeration but within the hour I wasn't able to make
        the conceptual leap to reduce the number of cases to check. I guess
        we just have to settle for minimising storage costs.
        """

        return []
