package programmers.난이도별.level03.불량_사용자;

import java.util.regex.*;
import java.util.stream.*;
import java.util.*;

class Solution1 {
    private boolean[] visited;
    private HashSet<String> set;
    private int target;
    private List<List<String>> possible_id;

    public List<String> cloneList(List<String> original, String str) {
        List<String> cloned_list = new ArrayList<String>(original);
        cloned_list.add(str);
        return cloned_list;
    }

    public String getRegex(String banned_id) {
        return "^" + banned_id.replaceAll("\\*", ".") + "$";
    }

    public void checkPossibleAnswer(List<String> list) {
        set.add(list.stream().sorted().collect(Collectors.joining("")));
    }

    public int solution(String[] user_id, String[] banned_id) {
        possible_id = Arrays.stream(banned_id).map(b_id -> {
            String REGEX = getRegex(b_id);
            return Arrays.stream(user_id).filter(u_id -> Pattern.matches(REGEX, u_id)).collect(Collectors.toList());
        }).collect(Collectors.toList());

        target = banned_id.length;
        visited = new boolean[target];
        set = new HashSet<>();
        dfs(0, new ArrayList<String>());
        return set.size();
    }

    public void dfs(int idx, List<String> list) {
        if (idx == target) {
            checkPossibleAnswer(list);
            return;
        }
        for (String str : possible_id.get(idx)) {
            if (list.indexOf(str) == -1)
                dfs(idx + 1, cloneList(list, str));
        }
    }
}

// https://leveloper.tistory.com/152 풀이 참고

class Solution2 {
    private String[] u_id;
    private String[] b_id;
    private int len;
    private int target;
    private boolean[] visited;
    private HashSet<HashSet<Integer>> resultSet;

    public int solution(String[] user_id, String[] banned_id) {
        u_id = user_id;
        visited = new boolean[user_id.length];
        resultSet = new HashSet<>();
        b_id = Arrays.stream(banned_id).map(v -> "^" + v.replace("*", ".") + "$").toArray(String[]::new);
        target = b_id.length;
        len = user_id.length;
        dfs(0, new HashSet<>());
        return resultSet.size();
    }

    private void dfs(int index, HashSet<Integer> set) {
        if (index == target) {
            resultSet.add(set);
            return;
        }
        for (int i = 0; i < len; i++) {
            if (Pattern.matches(b_id[index], u_id[i]) && !visited[i]) {
                visited[i] = true;
                set.add(i);
                dfs(index + 1, new HashSet<>(set));
                visited[i] = false;
                set.remove(i);
            }
        }
    }
}