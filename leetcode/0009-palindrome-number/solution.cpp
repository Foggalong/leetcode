class Solution {
public:
    bool isPalindrome(int x) {
        /*
            returns True if integer x is a palindrome (i.e. it
            reads the same left-to-right as right-to-left) and
            False otherwise. Does this without converting x to
            a string, list, or other object.
        */

        // negative numbers cannot be palindromes
        if (x < 0) return false;

        // handle zero specifically to avoid log issues
        if (x == 0) return true;

        // work out the number of digits
        const int n = log10(x) + 1;

        for (unsigned i = 1; i < (n/2)+1; i++) {
            // compute the ith digit
            const int frnt_digit = (int)(x / pow(10, n-i)) % 10;
            // compute the (n-i)th digit
            const int back_digit = (int)(x % (int)(pow(10, i))) / pow(10, i-1);
            // if two aren't equal, done
            if (frnt_digit != back_digit) return false;
        }
        return true;
    }
};
