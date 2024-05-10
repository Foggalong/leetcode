class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given a ascending list of integers, remove any
        duplicate entries in place and return the number
        of unique entries as an integer.
        """

        # guaranteed at least one entry
        value = nums[0]
        # start iterating from the second entry
        index = 1          

        while index < len(nums):
            # if same as previous, remove
            if nums[index] == value:
                nums.pop(index)
            # if different, move onto next
            else:
                value = nums[index]
                index += 1
        
        return index
