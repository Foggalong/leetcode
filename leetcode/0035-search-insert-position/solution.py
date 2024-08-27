class Solution:
    """
    Given a sorted array of distinct integers and a target value,
    returns the index of the target or otherwise the index where
    it would be if it were inserted in order.
    """

    def searchInsertSlow(self, nums: List[int], target: int) -> int:
        # does this in O(n)
        n = len(nums)
        for i in range(n):
            if nums[i] >= target: return i
        return n

    def searchInsert(self, nums: List[int], target: int) -> int:
        # does this in O(log n)

        l_index = 0            # index of lower bound
        r_index = len(nums)-1  # index of upper bound

        while True:
            # if lower bound >= target, target placed before lower bound 
            if nums[l_index] >= target: return l_index
            # if upper bound = target, found it! 
            if nums[r_index] == target: return r_index
            # if upper bound < target, target placed after upper bound 
            if nums[r_index] < target: return r_index + 1
            # if upper and lower bound adjacent, placed between them
            if r_index - l_index == 1: return r_index
            # find index of middle value
            m_index = l_index + int((r_index-l_index)/2)
            # if middle value < target, make middle value new lower bound
            if nums[m_index] < target:
                l_index = m_index
            # if middle value > target, make middle value new upper bound
            elif nums[m_index] > target:
                r_index = m_index
            # if middle value = target, lucked out and found it
            else:
                return m_index
