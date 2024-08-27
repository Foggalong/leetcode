using std::map;
using std::next;

class Solution {
public:
    int romanToInt(string s) {
        /*
            Takes a Roman numeral as string input and returns
            the integer value of that Roman numeral.
        */

        unsigned total = 0;     // running total
        unsigned position = 0;  // current position in string

        // numerals which can't be a subtraction prefix
        const map<char, unsigned> basic_numerals = {
            {'M', 1000}, {'D', 500}, {'L', 50}, {'V', 5}
        };

        // numerals which can be a subtraction prefix
        const map<char, unsigned> subtracting_numerals = {
            {'C', 100}, {'X', 10}, {'I', 1}
        };

        // numerals pairs which represent a subtraction
        const map<string, unsigned> subtracted_numerals = {
            {"CM", 900}, {"CD", 400},
            {"XC", 90},  {"XL", 40},
            {"IX", 9},   {"IV", 4}
        };

        bool possible_subtraction = false;
        char last_numeral;

        // iterate over the positions
        for(char& numeral : s) {
            // first, handle possible subtraction detected last iteration
            if (possible_subtraction) {
                // reset the flag
                possible_subtraction = false;
                // list of characters can become a string
                const string numeral_pair {last_numeral, numeral};
                if (subtracted_numerals.count(numeral_pair)) {
                    total += subtracted_numerals.at(numeral_pair);
                    position++; continue;  // don't double count this numeral
                } else {
                    total += subtracting_numerals.at(last_numeral);
                }
            }

            // cases w/o needing subtraction checks
            if (basic_numerals.count(numeral)) {
                total += basic_numerals.at(numeral);
            // cases where a substraction prefix is the last numeral
            } else if (position + 1  == s.size()) {
                total += subtracting_numerals.at(numeral);
                break;
            //  case where it's possible subtraction is occuring
            } else {
                possible_subtraction = true;
                last_numeral = numeral;
                // actual handling done at the top of next iteration
            }

            // advance to next position in string
            position++;
        }

        return total;
    }
};



