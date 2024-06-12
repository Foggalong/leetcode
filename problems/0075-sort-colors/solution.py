class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # object color counts, quicker than three L.count(x)
        color: dict[int, int] = {0: 0, 1: 0, 2: 0}
        for obj in nums:
            color[obj] += 1

        # color first `color[0]` objects in red
        nums[:color[0]] = [0]*color[0]
        # color next `color[1]` objects in white
        rw_index: int = color[0] + color[1]
        nums[color[0]:rw_index] = [1]*color[1]
        # color last `color[2]` objects in blue
        nums[rw_index:] = [2]*color[2]

