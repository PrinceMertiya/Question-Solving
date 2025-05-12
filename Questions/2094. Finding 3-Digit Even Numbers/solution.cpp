#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        set<int> res;
        int n = digits.size();

        for(int i = 0 ; i<n ; i++){
            for(int j = 0 ; j<n ; j++){
                for(int k = 0 ; k<n ; k++){

                    if(i == j || j == k || k == i){
                        continue;
                    }

                    if(digits[i] == 0){
                        continue;
                    }
                    if(digits[k] % 2 != 0 ){
                        continue;
                    }

                    int num = digits[i] * 100 + digits[j] * 10 + digits[k];
                    res.insert(num);
                }
            }
        }
        return vector<int>(res.begin(),res.end());
    }
};