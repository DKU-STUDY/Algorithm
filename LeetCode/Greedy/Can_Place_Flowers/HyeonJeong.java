package LeetCode.Greedy.Can_Place_Flowers;

class HyeonJeong {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int len = flowerbed.length;
        if (n == 0) // 심을 꽃이 없는 경우
            return true;
        if (len == 1) { // 주어진 화단이 1자리인 경우
            if (flowerbed[0] == 0 && n == 1)
                return true;
            else
                return false;
        }

        int result = 0, j = 0;
        if (flowerbed[0] + flowerbed[1] == 0) { // 화단의 첫 번째 자리에 심을 수 있는 경우
            flowerbed[0] = 1;
            result += 1;
        }
        if (flowerbed[len-2] + flowerbed[len-1] == 0) { // 화단의 마지막 자리에 심을 수 있는 경우
            flowerbed[len-1] = 1;
            result += 1;
        }
        if (result >= n)
            return true;

        while (j < n) {
            for (int i = 1; i < len-1; i++) {
                if (flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] == 0) { // 2 ~ (끝-1) 번째 자리에 꽃을 심을 수 있는 경우
                    flowerbed[i] = 1;
                    result += 1;
                }
                if (result == n)
                    return true;
            }
            j++;
        }
        return false;
    }
}
