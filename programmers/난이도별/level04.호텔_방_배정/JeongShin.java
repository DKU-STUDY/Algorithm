import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

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
        return IntStream.range(0, room_number.length)
                .mapToLong(i -> find(rooms, room_number[i]))
                .toArray();
    }
}
