class Solution {
public:
    

    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        stack<int> maxes;
        vector<bool> ar;  

        int maxVal = *max_element(candies.begin(), candies.end());
        for(size_t i = 0; i < candies.size(); i++) {
            int s = candies[i] + extraCandies;
            if(s >= maxVal)
               ar.push_back(true);
            else ar.push_back(false);
        }
        return ar;
    }
};