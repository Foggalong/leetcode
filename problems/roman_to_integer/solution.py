class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Takes a Roman numeral as string input and returns the integer value
        of that Roman numeral.
        """

        total = 0     # running total
        position = 0  # current position in string

        # numerals which can't be a subtraction prefix
        basic_numerals = {"M": 1000, "D": 500, "L": 50, "V": 5}
        # numerals which can be a subtraction prefix
        subtracting_numerals = {"C": 100, "X": 10, "I": 1}
        # numerals pairs which represent a subtraction
        subtracted_numerals = {
            "CM": 900, "CD": 400,
            "XC": 90,  "XL": 40,
            "IX": 9,   "IV": 4
        }
        
        # iterate over the positions
        while position < len(s):
            # save to avoid repeated access
            numeral = s[position]
    
            # cases w/o needing subtraction checks
            if numeral in basic_numerals:
                total += basic_numerals[numeral]
            
            # cases where a substraction prefix is the last numeral
            elif position + 1 == len(s):
                total += subtracting_numerals[numeral]
                break

            # case where it's possible subtraction is occuring
            else:
                # save to avoid repeated access
                numeral_pair = s[position:position+2]
                if numeral_pair in subtracted_numerals:
                    total += subtracted_numerals[numeral_pair]
                    position += 1  # don't double count next numeral
                else:
                    total += subtracting_numerals[numeral]
            
            # advance to next position in string
            position += 1

        return total