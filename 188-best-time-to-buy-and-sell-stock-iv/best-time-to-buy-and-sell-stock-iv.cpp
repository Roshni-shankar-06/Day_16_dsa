class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        if (k >= prices.size() / 2) {
            int sell = 0;
            int hold = INT_MIN;
            for (const int price : prices) {
                sell = max(sell, hold + price);
                hold = max(hold, sell - price);
            }
            return sell;

