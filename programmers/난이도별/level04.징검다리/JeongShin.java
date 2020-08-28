import java.util.*;

class Solution {
    public boolean checkPossible(List<Integer> rocksList, int min, int len, int n) {
        int removed = 0;
        int prev = 0;
        for (int curr : rocksList) {
            int distance = curr - prev;
            if (distance < min)
                removed++;
            prev = distance < min ? prev : curr;
            if (removed > n)
                return false;
        }
        return true;
    }

    public int solution(int distance, int[] rocks, int n) {
        List<Integer> rocksList = new ArrayList<>();
        for (int r : rocks)
            rocksList.add(r);

        int answer = 0;
        int low = 1;
        int high = distance;
        int size = rocksList.size();

        Collections.sort(rocksList);

        while (low <= high) {
            int mid = (high + low) / 2;
            if (checkPossible(rocksList, mid, size, n)) {
                answer = mid;
                low = mid + 1;
                continue;
            }
            high = mid - 1;
        }
        return answer;
    }
}
