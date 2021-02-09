package LeetCode.Array.Arranging_Coins;

class HyeonJeong {
    public int arrangeCoins(int n) {
        // 이진 탐색 이용
        long left = 0, right = n, value, x;
        while (left <= right) {
            x = left + (right - left) / 2;
            value = x * (x + 1) / 2;

            if (value == n)
                return (int)x;
            else if (value > n)
                right = x-1;
            else
                left = x+1;
        }
        return (int)right;
    }
}
