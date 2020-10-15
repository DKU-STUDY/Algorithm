import java.util.Arrays;
import java.util.HashMap;

public class sjjyy {
    public static int solution(String[][] clothes) {
        int answer = 1; // multiple
        HashMap<String, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < clothes.length; i++)
            hashMap.put(clothes[i][1], hashMap.getOrDefault(clothes[i][1], 0) + 1);
        // 같은 종류의 의상이라면 + 1

        for (int i : hashMap.values())
            answer *= (i + 1);
        // 총 경우의 수 *= (의상 개수 + 입지 않을 경우)

        return answer - 1;
        // 전부 입지 않는 경우 제외
    }

    public static void main(String[] args) {
        String[][] clothes1 = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        String[][] clothes2 = {{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};
        System.out.println(solution(clothes1)); // 5
        System.out.println(solution(clothes2)); // 3
    }
}
