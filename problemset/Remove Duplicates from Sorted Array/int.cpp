class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int c =1;
        //finding unique elements :
        for(int i = 0;i<nums.size()-1;i++)
        {
            if(nums[i] != nums[i+1])
            {
                nums[c] = nums[i+1];
                c++;
            }
        }
        return c;
    }
};