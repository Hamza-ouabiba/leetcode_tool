class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
         int n1 = INT_MAX;
         int n2 = INT_MAX;
         for(int i=0;i<nums.size();i++) {
             if(nums[i] > n2) return true;
             if(nums[i] <= n1) n1 = nums[i];
             else if(nums[i] <= n2) n2 = nums[i];
         }
         return false;
    }
};