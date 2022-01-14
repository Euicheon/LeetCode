class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for (int i = 0; i < numbers.size(); i++) {
          if (i>0 && numbers[i]==numbers[i-1]) {
              continue;
          }
          for (int j = i+1; j < numbers.size(); j++) {
              if (numbers[i]+numbers[j] == target) {
                  vector<int> vect;
 
                  vect.push_back(i+1);
                  vect.push_back(j+1);
                  return vect;
              }
          }
        }
        return numbers;

    }
};