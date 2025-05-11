#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int count = 0;
        for(int i = 0 ; i < arr.size() - 1 ; i++){
            if(arr[i] % 2 != 0){
                count++;
            }
                if(count == 3 ){
                    return true;
                }
        }
        return false;
    }
};