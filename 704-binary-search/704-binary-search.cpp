class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size()-1;
        while (l!=r) {
            int i = (l+r)/2;
            // std::cout << i << "  nums[i] = " << nums[i];
            if (nums[i]<target) {
                l = i + 1;
            } else if (nums[i]>target) {
                r = i;
            } else if (nums[i] == target) {
                return i;
            }
        }
        if (nums[l] == target) {
            return l;
        }
        return -1;
    }
};