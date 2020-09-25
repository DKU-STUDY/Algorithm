import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<Integer>();
        if(arr.length > 0) list.add(arr[0]); 
        
        for(int i=1; i<arr.length; i++) if(! list.get(list.size()-1).equals(arr[i])) list.add(arr[i]); 
        
        int[] newArr = new int[list.size()]; 
        for(int i=0; i<newArr.length; i++) newArr[i] = list.get(i);
        
        return newArr;
	}
}
