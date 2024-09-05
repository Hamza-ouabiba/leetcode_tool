class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int isola = 0;
        int count = 0;
        int all = 0;
        int samLi = 0;
        for(int i = 0;i<grid.size();i++)
        {
            for(int j = 0;j<grid[0].size();j++)
            {
                if(grid[i][j] == 1)
                {
                    all++;
                    count = 0;
                    samLi = 0;
                    for(int z=0;z<grid.size();z++)
                    {
                        if(grid[z][j] == 1)
                            count++;
                    }
                    for(int k = 0;k<grid[0].size();k++)
                    {
                        if(grid[i][k] == 1)
                            samLi++;
                    }
                    if((count+samLi)-1 == 1)
                        isola++;
                }
            }
        }
        return all-isola;
    }
};