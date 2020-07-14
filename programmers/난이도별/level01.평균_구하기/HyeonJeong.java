package 난이도별.level01.평균_구하기;

public class HyeonJeong {
    class Solution {
        public double solution(int[] arr) {
            double average;
            double total = 0;

            for(int i = 0; i < arr.length; i++)
                total += arr [i];
            average = total / arr.length;
            return average;
        }
    }
}
