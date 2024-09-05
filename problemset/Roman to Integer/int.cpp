class Solution {
public:
    int romanToInt(string s) {
            int sum = 0;
            int i;
            for( i=0;i<s.size();i++) {
                if(s[i] == 'C' && s[i+1] == 'M') {
                    sum+=900;
                    i++;
                    continue;
                } else if(s[i] == 'C' && s[i+1]  == 'D') {
                    sum+=400;
                    i++;
                    continue;
                } else if(s[i]  == 'I' && s[i+1]  == 'V') {
                    sum+=4;
                    i++;
                    continue;
                } else if(s[i]  == 'I' && s[i+1] == 'X'){
                    sum+=9;
                    i++;
                    continue;
                } else if(s[i]  == 'X' && s[i+1]  == 'L') {
                    sum+=40;
                    i++;
                    continue;
                } else if(s[i] == 'X' && s[i+1]  == 'C') {
                    sum+=90;
                    i++;
                    continue;
                    }
                switch(s[i] ) {
                        case 'I': sum+=1;break;
                        case 'V': sum+=5;break;
                        case 'X': sum+=10;break;
                        case 'L': sum+=50;break;
                        case 'C': sum+=100;break;
                        case 'D': sum+=500;break;
                        case 'M': sum+=1000;break;
                }
            }
            return sum;
        }
};