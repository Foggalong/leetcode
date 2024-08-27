class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Given two arrays of integers, the latter contained in the former, sort
        the entries of the former by their position in the latter. Entries which
        don't appear in the latter are at the end in ascending order. 
        """

        return sorted(arr1, key=lambda entry: self.position(arr2, entry))


    def position(self, array: List[int], integer: int):
        """
        Given an array of integers and a specific integer, return the position
        of that integer in the array. If it doesn't feature return 1000 (the
        maximum possible length of the array) plus the value of the integer.
        """

        try:
            return array.index(integer)
        except ValueError:
            return 1000 + integer

