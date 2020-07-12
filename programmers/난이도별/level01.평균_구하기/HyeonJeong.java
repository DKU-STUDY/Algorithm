package 난이도별.level01.평균_구하기;

public class HyeonJeong {
    class Solution {
        public double solution(int[] arr) {
            float average;
            float total = 0;

            for(int i = 0; i < arr.length; i++)
                total += arr [i];
            average = total / arr.length;
            return average;
        }
    }
}

/*
문제 설명
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

제한사항
arr은 길이 1 이상, 100 이하인 배열입니다.
arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
 */