class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        
        int total = 0;
        for (int i = 0; i < k ; i++ ){
            total += nums[i];
        }
        int max_sum = total;
        for(int i = k ; i < nums.size() ; i++){
            total += nums[i] - nums[i-k];
            max_sum = max(total, max_sum);



        }
        return (double)max_sum / k;
    }
};