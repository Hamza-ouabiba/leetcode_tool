class Solution {
public:

    int mySqrt(int x) {
        long num = -1;
        int right = 0;
        int left = x;
        //binary search : 
        while(right <= left)
        {
            long mid = (right + left) / 2;
            if(mid * mid == x)
                return (int)mid;
            else if(mid *mid < x)
            {
                right = mid + 1;
            } else 
            {
                left = mid -1;
            }
        }
        for(long i = 1;i<=x;i++)
        {
            if(i * i > x)
            {
                num = i-1;
                break;
            }
        }
        return (int)num;
    }
};