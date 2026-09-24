class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (k >= prices.size() / 2) {
            int sell = 0;
            int hold = INT_MIN;
         
