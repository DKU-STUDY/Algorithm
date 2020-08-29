import java.util.*;

class Solution {
    public long find(Map<Long, Long> rooms, long num) {
        Long parent = rooms.get(num);
        if (parent == null) {
            rooms.put(num, num + 1);
            return num;
        }
        parent = find(rooms, parent);
        rooms.put(num, parent);
        return parent;
    }

    public long[] solution(long k, long[] room_number) {
        Map<Long, Long> rooms = new HashMap<Long, Long>();
        int len = room_number.length;
        long[] answer = new long[len];

        for (int i = 0; i < len; i++)
            answer[i] = find(rooms, room_number[i]);

        return answer;
    }
}
