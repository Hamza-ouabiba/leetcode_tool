class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int c = 0;
        int taille = nums.size();
        for(int i = 0;i<taille;i++)
        {
            if(nums[i] == val)
            {
                for(int j = i;j<taille-1;j++)
                    nums[j] = nums[j+1];
                taille--;
                i--;
            }
        }
        return taille;
    }
};