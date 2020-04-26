// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int n)
    {
        int gap = 0;
        int temp = 0;
        
        if (n == 1)
            return 0; // 1 = 0
        
        char binary[] = Integer.toBinaryString(n).toCharArray(); // binary로 변환 후 char[] 배열 생성
        
        for (int x = 0; x < binary.length; x++)
        {
            if(binary[x] == '0')
            {
                temp++; // count 0
                continue;
            }
            else if(binary[x] == '1') // end
            {
                if(temp > gap)
                gap = temp;
                temp = 0;
            }
        }
        return gap;
    }
}
