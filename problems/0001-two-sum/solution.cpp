class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /*
            Take a list of integers (nums) and an integer (target)
            as input and then returns vector {i,j} where we have
            nums[i] + nums[j] == target. If such a pair does not
            exist, an empty vector is returned.
        */

        // create a location map, O(n)
        map<int, int> locations;
        for (int i = 0; i < nums.size(); i++) {
            locations[nums.at(i)] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            try {
                // try to access j from the location map 
                const int j = locations.at(target - nums.at(i));
                // can't reuse values
                if (j == i) continue;
                // if error wasn't thrown, done!
                return {i, j};
            } catch (const std::out_of_range& oor) {
                continue;
            }
        }

        // return empty vector if no solution found
        return {};
    }
};

