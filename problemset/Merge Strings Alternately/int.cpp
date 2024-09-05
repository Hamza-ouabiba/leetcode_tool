class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int size = word1.size() > word2.size() ? word1.size() : word2.size();
        string s = "";
        for(int i=0;i<size;i++) {
            if(i < word1.size()) s+=word1[i];
            if(i < word2.size()) s+=word2[i];
        }
        return s;
    } 
};