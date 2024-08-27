class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        Return the number of increments and/or decrements necessary to
        transform a list of integers (`students`) into another list of
        integers (`seats`). O(nlogn) time, O(n) storage.
        """ 

        # match the ith smallest student to the ith smallest seat 
        srt_seat: iter[int] = sorted(seats)
        srt_stud: iter[int] = sorted(students)

        return sum(abs(srt_seat[i] - srt_stud[i]) for i in range(len(seats)))
