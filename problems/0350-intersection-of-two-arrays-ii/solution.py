class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Returns the intersection of two lists of integers, accounting for
        duplicates. Destructive algorithm for `nums1`.
        """

        intersection: List[int] = []
        for n in nums2:
            if n in nums1:
                intersection.append(n)
                nums1.remove(n)

        return intersection

            
