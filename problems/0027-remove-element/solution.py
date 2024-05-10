class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Given a list of integers and an integer, remove any
        list entries which are equal to that integer in-place
        and return the number of remaining entries as an int.
        """

        index = 0    
        while index < len(nums):
            # if same as value, remove
            if nums[index] == val:
                nums.pop(index)
            # if different, move onto next
            else:
                index += 1
        
        return index
