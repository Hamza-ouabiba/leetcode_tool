class Solution {
public:
    string reverseWords(string s) {
        vector<string> st;
        string f = "";
        for(int i=0;i<s.size();i++) {
            if(s[i] != ' ') {
                f+=s[i];
            } else {
                    if(f != "") st.push_back(f);
                    f = "";
            }
            if(i == s.size() - 1 && f != "") st.push_back(f);
        }
        int t = st.size() -1;
        for(int i=0;i<st.size() / 2;i++){
            string temp = st[i];
            st[i] = st[t];
            st[t] = temp;
            t--;
        }
        f = "";
        for(int i=0;i<st.size();i++){
            if(i < st.size() - 1) f+=st[i]+' ';
            else f+=st[i];
        }
        return f;
    }
};