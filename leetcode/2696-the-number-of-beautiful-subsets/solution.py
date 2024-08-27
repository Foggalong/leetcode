class Solution:
    def beautifulSubsets(self, nums: List[int], k: int, index: int = 0, subset: List[int] = []) -> int:
        """
        Given an array nums of positive integers and a positive integer k,
        returns the number of non-empty beautiful subsets. A subset is
        beautiful if it does not contain two integers with an absolute
        difference equal to k.

        This function does this by iterating through the numbers `m` by their
        index in `nums` by recursive calls of `beautifulSubsets`, starting
        with the first element (hence the default value of `index=0`.
        """

        # check if we've reached the end of `nums`
        if index == len(nums):
            # if subset != [], add one for the current value of `subset`
            if subset:
                return 1
            # if subset == [], must be our initial start before backtracking
            # so we haven't yet found anything to add to the tally
            else:
                return 0

        # this is NOT as size, it's an actual number in nums 
        m: int = nums[index]

        # count beautiful subsets which don't include `m`
        without_m: int = self.beautifulSubsets(nums, k, index+1, subset)

        # handle case where `m` appears more than once in nums
        if m in subset: return 2 * without_m
            
        # count beautiful subsets after adding `m`, skipping those which
        # already contain an n such that abs(m-n) = k.
        with_m: int = 0
        if not (m-k in subset or m+k in subset):
            with_m = self.beautifulSubsets(nums, k, index+1, subset+[m])

        return without_m + with_m


    def failedBeautifulSubsets(self, nums: List[int], k: int) -> int:
        """
        This was my first attempt but, while it gets the correct solution,
        it unfortunately takes too long to complete the challenge so a new
        approach was needed.

        This doesn't use the method for finding subsets I used in previous
        problems, but a new method using a sequence of binary numbers. I
        saw this discussed in the comments after the last subset challenege.
        """

        n: int = len(nums)

        # handle the degenerate case (no chance for ugly pairs)
        if n == 1: return 1

        # create a list of all pairs which stop nums being beautiful
        ugly_pairs_dict: dict[int: List[int]] = {}
        for a in nums:
            ugly_pairs_dict[a] = [b for b in nums if abs(a-b) == k]

        beautiful_count: int = 0

        # only interested in non-empty subsets, so start at 1
        for i in range(1, 2**n):
            # convert i to an n-bit binary string
            filter: str = f"{i:b}".zfill(n)
            # use this binary string to filter nums to a subset
            subset: List[int] = [nums[j] for j in range(n) if filter[j] == '1']

            # if contains both digits from any ugly pair, it's not beautiful
            beautiful = True
            for a in subset:
                if any(b in subset for b in ugly_pairs_dict[a]):
                    beautiful = False
                    break

            # if did not contain any ugly pairs, must be beautiful
            if beautiful: beautiful_count += 1

        return beautiful_count
