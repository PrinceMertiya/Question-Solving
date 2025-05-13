class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> hashed;

        for (int i = 0 ; i < nums.size() ; i++){
            int val = nums[i];
            int complement = target - val;

            if(hashed.find(complement) != hashed.end()){

                return {hashed[complement] ,i};
            }

            hashed[val] = i;
            }

            return {};

    }
};