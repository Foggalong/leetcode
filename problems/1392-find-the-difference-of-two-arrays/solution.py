class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """
        Takes two lists, nums1, nums2, as inputs and then returns
        two lists, the first being the items which exclusively
        appear in nums1 and the second being those which appear
        exclusively in nums2.
        """

        # create dict entry for each item in nums1
        nums1only = {}
        for num in nums1:
            # assumption everything only in nums1
            nums1only[num] = True

        nums2only = []
        for num in nums2:
            # if num exists in nums1only, exists in both
            try:
                if nums1only[num]:
                    nums1only[num] = False
            # if num not in nums1only, in nums2only
            except KeyError:
                nums2only.append(num)
                nums1only[num] = False

        return [
            # if still True in nums1only, only in nums1
            [num for num in nums1only if nums1only[num]],
            nums2only
        ]
