class Solution {
public:
    string triangleType(vector<int>& nums) {
        int a = nums[0];
        int b = nums[1];
        int c = nums[2];


        if(a == b && b==c){
            return "equilateral";
        }

        else if( a == b || b == c || c == a){
            return "isosceles";
        }

        else if( a + b < c ){
            return "none";
        }

        else{
            return "scalene";
        }
    }
};