class Solution {
    public int numTrees(int n) {
        int[] memo = new int[n+1];

        Arrays.fill(memo,-1);
        return treed(memo,n);

    }
    public int treed(int[] memo , int n){
        if(n==0 || n==1){
            return 1;
        }

        if(memo[n] != -1){
            return memo[n];
        }

        int total = 0;
        for(int i = 1 ; i <= n ;i++){
            int left = treed(memo,i-1);
            int right = treed(memo,n-i);

            total += left*right;
            
        }
        memo[n] = total;
        return total;
    }
}