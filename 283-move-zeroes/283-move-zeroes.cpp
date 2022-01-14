class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        // int zero_i = 0;
        int count_zero = 0;
        for (int i=0; i<nums.size();i++) {
            if (nums[i]==0) {
                reverse(nums.begin()+i,nums.end()-count_zero);
                reverse(nums.begin()+i,nums.end()-1-count_zero);
                count_zero++;
                // auto res = split("test", 'a');
                // for ( auto const& item : nums )
                // {
                //    std::cout << item << " ";
                // }
                // std::cout << i << std::endl;
                if (nums[i]==0) {
                    i--;
                }
                if (nums.size()-count_zero == i){
                    break;
                }
            }
        }
        // return nums;
        // 001
        // 100
        // 010
        //
    }
};