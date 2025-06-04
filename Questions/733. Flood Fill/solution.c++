class Solution {

    void dfs(vector<vector<int>> &image , int sr, int sc, int color , int rows,int cols, int source){

        if(sr< 0 || sc < 0 || sr >= rows || sc >= cols){
            return ;

        }
        if(image[sr][sc] != source) return;

        image[sr][sc] = color;

        dfs(image,sr + 1,sc,color,rows,cols,source);
        dfs(image,sr - 1,sc,color,rows,cols,source);
        dfs(image,sr,sc + 1,color,rows,cols,source);
        dfs(image,sr ,sc - 1,color,rows,cols,source);
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        
        int rows =  image.size();
        int cols = image[0].size();
        int source = image[sr][sc];

        if(source == color) return image;

        dfs(image,sr,sc,color,rows,cols,source);

        return image;
    }
};