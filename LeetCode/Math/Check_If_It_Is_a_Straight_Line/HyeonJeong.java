package LeetCode.Math.Check_If_It_Is_a_Straight_Line;

import java.util.Arrays;

class HyeonJeong {
    public boolean checkStraightLine(int[][] coordinates) {
        int check = 0, len = coordinates.length;
        float [] slope = new float[len-1];

        for (int i = 1; i < len; i++) {
            if (coordinates[i-1][0] == coordinates[i][0])
                check += 1;
        }
        if (check == len-1) { // 주어진 [x,y]들로 x축과 평행한 직선이 만들어지는 경우
            return true;
        }
        else if (check != 0)
            return false;

        for (int i = 1; i < len; i++) // 기울기 값을 배열에 넣음
            slope[i-1] = (float)(coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0]);

        Arrays.sort(slope);
        if (slope[0] != slope[len-2]) // 가장 큰 값과 가장 작은 값을 비교해서 모두 같은 값을 가지는지 확인
            return false;
        return true;
    }
}
