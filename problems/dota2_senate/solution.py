
class Solution:
    def popChr(self, string: str, index: int) -> str:
        """
        Given a string and an index, return the string with
        the (index)th character removed.
        """
        return string[:index] + string[(index+1):]

    def predictPartyVictory(self, senate: str) -> str:
        """
        Given string encoding the composition of a Dota2
        senate, return which party would win a vote.
        """

        # counts of Radiants and Dires
        Rs = senate.count('R')
        Ds = len(senate) - Rs
        # running total of senators to ban
        banR = banD = 0

        # double while loop will ensure we keep iterating over
        # senators until a victor is determined
        while True:
            index = 0
            while index < len(senate):
                if senate[index] == 'R':
                    if banR:
                        senate = self.popChr(senate, index)
                        banR -= 1
                        continue
                    elif not Ds:
                        return 'Radiant'
                    else:
                        banD += 1
                        Ds -= 1
                else:  # senator == 'D'
                    if banD:
                        senate = self.popChr(senate, index)
                        banD -= 1
                        continue
                    elif not Rs:
                        return "Dire"
                    else:
                        banR += 1
                        Rs -= 1

                index += 1
