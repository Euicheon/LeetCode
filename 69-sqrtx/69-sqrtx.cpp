class Solution {
public:
    int mySqrt(int x) {
        int i = 1;
        while (i < 46341) {
            // cout << i << "\n";
            long long pow = i*i;
            if (pow > x) {
                return i-1;
            } else if ( pow == x ) {
                return i;
            } else {
                i++;
            }
        }
        return 46340;
    }
};