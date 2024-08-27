class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        // save length to avoid finding repeatedly
        unsigned n = nums.size();
        // initalise vector twice the length of nums
        vector<int> ans(2*n, 0);
        // only need to iterate over nums, not ans
        for (unsigned i = 0; i < n; i++) {
            ans[i]   = nums[i];
            ans[i+n] = nums[i];
        }
        return ans;
    }
};
