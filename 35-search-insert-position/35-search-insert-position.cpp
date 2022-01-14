class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size()-1;
        if (nums.back() < target) {
            return r+1;
        }
        while (r != l) {
            int flag = (l+r)/2;
            // cout << "l,r = " << l <<", " <<r<<'\n';
            if (nums[flag] < target) {
                l = flag + 1;
            } else if (nums[flag] > target) {
                r = flag;
            } else {
                return flag;
            }
        }
        
        return r;
    }
};