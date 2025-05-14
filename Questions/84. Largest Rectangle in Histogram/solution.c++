class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int MaxArea = 0 ; 
        stack<int> st;
        int n = heights.size();

        for(int i = 0 ; i <= n ; i++){

            int currentHeight = (i == n ) ? 0 : heights[i];

            while(!st.empty() && currentHeight < heights[st.top()]){
                int Index = st.top();
                int height = heights[Index];
                st.pop();
                int width;

                if(st.empty()){
                    width = i;

                }
                else{
                    width = i - st.top() - 1;

                }
                int area = width * height;
                MaxArea = max(MaxArea , area);
            }
            st.push(i);
        }
        return MaxArea;

    }
};