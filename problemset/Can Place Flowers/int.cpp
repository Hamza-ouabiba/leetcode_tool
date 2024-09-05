class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int c = 0;
        for (size_t i = 0; i < flowerbed.size(); i++) {
            bool check1 = false;
            bool check2 = false;
            if (flowerbed[i] == 0) {
                if (i + 1 < flowerbed.size()) {
                    if (flowerbed[i + 1] == 0)
                        check1 = true;
                } else 
                    check1 = true;

                if(i > 0) {
                    if (flowerbed[i - 1] == 0) 
                        check2 = true;
                } else check2 = true;
                if (check1 && check2) {
                    flowerbed[i] = 1;
                    c++;
                    if (c >= n) {
                        return true; 
                    }
                }
            }
        }
        return c >= n;
    }
};