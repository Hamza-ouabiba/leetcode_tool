class Solution {
public:
    int compress(vector<char>& chars) {
        vector<char> c;
        char fi = chars[0];
        c.push_back(fi);
        int co=1;
        for(int i=1;i<chars.size();i++) {
            if(fi == chars[i]) {
                co++;
            } else{
                if(co > 1) {
                    string count = to_string(co);
                    for (char ch : count) {
                        c.push_back(ch);
                    }
                }
                co=1;
                fi = chars[i];
                c.push_back(fi);
            }

             if(i == chars.size() -1 && co > 1) {
                string count = to_string(co);
                for (char ch : count) {
                    c.push_back(ch);
                }
             }
        }
        chars = c;
        return chars.size();
    }
};