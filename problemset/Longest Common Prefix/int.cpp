class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
            if(strs.size() == 0) return "";
            bool isPrefix = false;
            string prefix = strs[0];
            while(prefix.size() > 0) {
                int count=0;
                for(size_t i=1;i<strs.size();i++) {
                    if(prefix == strs[i].substr(0,prefix.size()))
                        count++;
                }
                if(count == strs.size()-1)
                    break;
                prefix = prefix.substr(0,prefix.size()-1);
            }
            return prefix;
        }
};