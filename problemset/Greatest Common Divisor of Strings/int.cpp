class Solution {
public:
    int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
    bool isGood(string str,string x) {
        int nbre = str.length() / x.length();
        int co = 0;
        for(int i=0;i<nbre;i++) {
            string te = str.substr(co,x.length());
            if(te != x)
               return false;
            co+=x.length();
        }
        return true;
    }
    string gcdOfStrings(string str1, string str2) {
        int pgcd = gcd(str1.length(),str2.length());
        string s = "";
        for(int i=0;i<pgcd;i++) 
           s+=str1[i];
        if(isGood(str1,s) && isGood(str2,s))
            return s;
        return "";
    }
};