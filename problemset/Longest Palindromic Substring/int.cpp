#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() <= 1) return s;
        
        int maxLength = 1; 
        int start = 0;    
        
        for (int i = 0; i < s.size(); ++i) {
            int left = i, right = i;
            while (left >= 0 && right < s.size() && s[left] == s[right]) {
                int currentLength = right - left + 1;
                if (currentLength > maxLength) {
                    maxLength = currentLength;
                    start = left;
                }
                --left;
                ++right;
            }
            
            left = i, right = i + 1;
            while (left >= 0 && right < s.size() && s[left] == s[right]) {
                int currentLength = right - left + 1;
                if (currentLength > maxLength) {
                    maxLength = currentLength;
                    start = left;
                }
                --left;
                ++right;
            }
        }
        
        return s.substr(start, maxLength);
    }
};