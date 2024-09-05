class Solution {
public:
    bool isPalindrome(int x) {
       vector<char> reverseString;
       stringstream ss;
       string str;
       ss << x;
       ss >> str;
       for(int i = str.size()-1;i>=0;i--)
           reverseString.push_back(str[i]);
       for(int i = 0;i<str.size();i++)
       {
           if(str[i] != reverseString[i])
             return false;
       }
       return true;
    }
};