class Solution {
public:
    int missingNumber(vector<int>& nums) {
        map<int,bool> mp;
        set<int> s;
        for(size_t i=0;i<nums.size();i++) {
            s.insert(nums[i]);
        }

        int t = s.size();
        int max = *max_element(nums.begin(),nums.end());
        if(max > t) t = max;

        for(size_t i=0;i<=t;i++) {
            mp.insert({i,false});
        }

        for(size_t i=0;i<nums.size();i++) {
            mp[nums[i]] = true;
        }

        for(const auto & elm : mp) {
            if(!elm.second) return elm.first;
        }
        return -1;
    }
};