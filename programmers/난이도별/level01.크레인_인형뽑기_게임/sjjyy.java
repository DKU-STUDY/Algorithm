package 난이도별.level01.크레인_인형뽑기_게임;

import java.util.Stack;

public class sjjyy
{
    public static int solution(int[][] board, int[] moves)
    {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();

        for (int i : moves)
        {
            for (int j = 0; j < board.length; j++)
            {
                if (board[j][i - 1] != 0)
                {
                    if (stack.empty()) // 바구니가 비었으면 인형을 넣음
                        stack.push(board[j][i - 1]);
                    else {
                        if (stack.peek() == board[j][i - 1]) // 바구니 맨 위쪽 인형과 넣은 인형이 같다면 제거
                        {
                            stack.pop();
                            answer += 2;
                        } else
                            stack.push(board[j][i - 1]); // 다르다면 인형을 넣음
                    }

                    board[j][i - 1] = 0; // 뽑기 기계 칸을 비움
                    break;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args)
    {
        int[][] board = new int[][]{
                {0, 0, 0, 0, 0},
                {0, 0, 1, 0, 3},
                {0, 2, 5, 0, 1},
                {4, 2, 4, 4, 2},
                {3, 5, 1, 3, 1}};
        int[] moves = new int[]{1, 5, 3, 5, 1, 2, 1, 4};

        System.out.println(solution(board, moves)); // 4
    }
}
