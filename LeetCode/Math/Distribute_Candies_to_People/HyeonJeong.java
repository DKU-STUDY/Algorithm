package LeetCode.Math.Distribute_Candies_to_People;

class HyeonJeong {
    public int[] distributeCandies(int candies, int num_people) {
        /*
        첫번째 사람부터 1개의 사탕을 주기 시작해서 1개씩 사탕을 늘려서 다음 사람에게 주고,
        마지막 사람에게 주고도 사탕이 남은 경우에는 다시 첫번째 사람에게 사탕을 나눠준 사탕의 배열을 반환하는 문제
         */
        int []result = new int[num_people];
        int n = 1, i = 0;
        while (true) {
            if (candies >= n) {
                result[i] += n;
                candies -= n;
                n += 1;
            }
            else {
                result[i] += candies;
                break;
            }
            i += 1;
            if (i == num_people) {
                i = 0;
            }
        }
        return result;
    }
}
