// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long long int first = 1;
        long long int end = n;
        while (first != end) {
            long long int check = (first + end)/2;
            if (isBadVersion(check)) {
                end = check;
            } else {
                first = check+1;
            }
        }
        return end;
    }
};