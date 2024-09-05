class Solution {
public:
    string reverseVowels(string s) {
        vector<int> v ;
        for(int i=0;i<s.size();i++) {
            if(tolower(s[i]) == 'e' || tolower(s[i])  == 'o' || tolower(s[i])  == 'a' 
                || tolower(s[i])  == 'i' ||tolower(s[i])  == 'u') {
                v.push_back(i);
            }
        }

        int t = v.size() - 1;
        for(int i=0;i<v.size() / 2;i++) {
            char temp = s[v[t]];
            s[v[t]] = s[v[i]];
            s[v[i]] = temp;
            t--;
        }
         return s; 
    }
};