import java.util.Arrays;

public class sjjyy {
    /*
        @param brown, yellow : 테두리는 갈색, 중앙은 노란색으로 칠해져있는 카펫
        갈색 격자의 수는 8이상 5,000 이하 자연수, 노란색 격자의 수는 1 이상 2,000,000 이하의 자연수
        카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 김.
        @return 카펫의 가로 세로 크기 배열
    */
    public static int[] solution(int brown, int yellow) {
        int width = 0, height = 0;

        for (int i = 1 ; i <= yellow / 2 + 1 ; i++) { // 노란색을 기준으로 탐색, 카펫이 직사각형이므로 yellow/2+1까지 탐색.
            width = i ;
            height = (yellow % i == 0) ? yellow / i : yellow / i + 1;

            if (2 * width + 2 *height + 4 == brown) // 테두리의 갈색은 노란색의 가로*2, 세로*2 + 모서리 4개의 개수와 같음
                break;
        }

        return new int[]{Math.max(width, height) + 2, Math.min(width, height) + 2}; // 가로가 세로보다 길거나 같음
    }

    public static void main(String [] args) {
        System.out.println(Arrays.toString(solution(10, 2))); // [4, 3]
        System.out.println(Arrays.toString(solution(8, 1))); // [3, 3]
        System.out.println(Arrays.toString(solution(24, 24))); // [8, 6]
    }
}
