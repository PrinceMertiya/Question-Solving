class Solution {
public:
    long long distributeCandies(int n, int limit) {
        vector<vector<long long>> dp(4,vector<long long>(n + 1, 0));

        dp[0][0] = 1 ;

        for(int i = 1 ; i <=  3 ; i++){
            for (int sum = 0 ; sum <= n ; sum++){
                for(int x = 0 ; x <= min(limit,sum) ; x++){
                    dp[i][sum] += dp[i - 1][sum - x];
                }
            }
        }
        return dp[3][n];
    }
};