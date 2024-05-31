class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, in which exactly two elements
        appear only once and all the other elements appear exactly
        twice. Find the two elements that appear only once. You can
        return the answer in any order.
        """

        # exactly two elements appear once
        singletons: List[int] = []

        # convert nums to heap (linear time) and extract lowest
        heapify(nums)
        last_x = heappop(nums)

        while nums:
            # if smallest in heap not the same as the last, the
            # last must have been a singleton
            x = heappop(nums)
            if x != last_x:
                singletons.append(last_x)
                # only two singletons to find
                if len(singletons) == 2: return singletons
            # otherwise move onto the next element, which since
            # elements appear exactly once or twice, will be new
            else:
                x = heappop(nums)
            # in either case, the last x examined will become
            # the one to check against next iteration
            last_x = x

        # handle the case where the last in nums was a singleton,
        # so was never compared
        return singletons + [last_x]

