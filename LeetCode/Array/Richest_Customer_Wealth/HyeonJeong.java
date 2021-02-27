package Richest_Customer_Wealth;

class HyeonJeong {
    public int maximumWealth(int[][] accounts) {
        int []sum = new int[accounts.length];
        int result = 0;
        for (int i = 0; i < accounts.length; i++) {
            sum[i] = 0;
            for (int j = 0; j < accounts[0].length; j++) {
                sum[i] += accounts[i][j];
            }
            if (sum[i] > result)
                result = sum[i];
        }
        return result;
    }
}
