class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> ans;
        vector<int>::iterator it = nums.begin();
        while (nums.size() > 1) {
            it = nums.begin();
            if (abs(nums.front()) > abs(nums.back())) {
                int temp = nums.front();
                nums.erase(nums.begin());
                // it = ans.insert(it, temp*temp);
                auto it = ans.insert(ans.begin(), temp*temp);
            } else {
                int temp = nums.back();
                nums.pop_back();
                auto it = ans.insert(ans.begin(), temp*temp);
            }
        }
        int temp = nums.back();
        it = ans.insert(ans.begin(), temp*temp);
        return ans;
    }
};