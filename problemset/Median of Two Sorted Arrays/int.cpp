class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> mergeArray;
        int j =0;
        for(int i = 0;i<nums1.size();i++)
            mergeArray.push_back(nums1[i]);
        for(int i = 0;i<nums2.size();i++)
            mergeArray.push_back(nums2[j++]);
        sort(mergeArray.begin(),mergeArray.end());
        if(mergeArray.size() % 2 == 0)
        {
            int l1 = mergeArray[(mergeArray.size()/2)-1];
            int l2 = mergeArray[mergeArray.size()/2];
            return (l1+l2)/2.0;
        } else
            return mergeArray[mergeArray.size()/2];
    }
};