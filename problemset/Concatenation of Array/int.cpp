class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int i = 0;
        int count = 0;
        while(count < 2 * nums.size())
        {
             if(i == (nums.size())) 
                i = 0;
            ans.push_back(nums[i]);
            count ++;
            i++;
        }
        return ans;
    }
};