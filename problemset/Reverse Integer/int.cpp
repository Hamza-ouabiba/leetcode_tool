class Solution {
public:
    int reverse(int x) {
           int j = 0;
            long sum = 0;
            int siz;
            vector<int> reverseInt;
            while(x)
            {
                reverseInt.push_back(x%10);
                x = x / 10;
            }
            siz = reverseInt.size()-1;
            for(int i = 0;i<reverseInt.size();i++)
            {
                sum+=reverseInt[i] * pow(10,siz);
                siz--;
            }
            if(sum > INT_MAX || sum < INT_MIN) return 0;
            return (int)sum;
    }
};