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
        }
        vector<int> sell(k + 1, 0);
        vector<int> hold(k + 1, INT_MIN);
        for (const int price : prices) {
            for (int i = k; i > 0; --i) {
            
