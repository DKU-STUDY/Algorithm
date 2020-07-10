package 난이도별.level01.같은_숫자는_싫어;

import java.util.ArrayList;
import java.util.Arrays;

public class sjjyy
{
    public static int [] solution(int[] array)
    {
        ArrayList<Integer> arrayList = new ArrayList<>();
        int len = array.length - 1;

        for(int i = 0 ; i < len ; i++)
        {
            if(array[i] != array[i+1])
                arrayList.add(array[i]);
        }

        arrayList.add(array[len]); // 마지막 인덱스 값

        int aLen = arrayList.size();
        int[] ans = new int[aLen];
        for(int i = 0 ; i < aLen ; i++) ans[i] = arrayList.get(i);

        return ans;
    }

    public static void main(String [] args)
    {
        int[] arr = {1, 1, 3, 3, 0, 1, 1};
        System.out.println(Arrays.toString(solution(arr))); // [1, 3, 0, 1]
    }
}
