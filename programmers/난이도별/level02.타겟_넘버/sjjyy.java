public class sjjyy {
    /*
        https://programmers.co.kr/learn/courses/30/lessons/43165
        @param numbers : n개의 음이 아닌 정수
        이 수를 적절히 더하거나 빼서 타겟넘버 target을 만듦
        @return 타겟넘버를 만드는 경우의 수
    */
    public static int solution(int[] numbers, int target) {
        return DFS(numbers, target, 0, 0);
    }

    private static int DFS(int[] numbers, int target, int index, int num) { // 깊이 우선 탐색으로 모든 경우의 수를 구함
        if (index == numbers.length)
            return num == target ? 1 : 0; // 타겟넘버와 같으면 + 1

        return DFS(numbers, target, index + 1, num + numbers[index]) // 왼쪽 노드
                + DFS(numbers, target, index + 1, num - numbers[index]); // 오른쪽 노드
    }

    public static void main(String[] args) {
        int[] numbers = {1, 1, 1, 1, 1};
        System.out.println(solution(numbers, 3)); // 5
    }
}
