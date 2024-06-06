from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Return True if it's possible to rearrange `hand` into straights
        of size `groupSize`, false otherwise.
        """
 
        # handle trivial case where groupSize doesn't divide hand size
        if len(hand) % groupSize: return False
        
        # # track how many of each card value are in the hand
        counts: dict[int, int] = Counter(hand)
        
        # check possible cards to start straights in ascending order
        for start in sorted(hand):
            # skip if no cards left of this value
            if not counts[start]: continue

            # check all intermediate cards neccessary for a straight
            if any(not counts[i] for i in range(start, start+groupSize)):
                return False

            # if all there, set them aside as used
            for i in range(start, start + groupSize): counts[i] -= 1

        # if reached here, must have been possible to split everything
        # nicely into straights
        return True
