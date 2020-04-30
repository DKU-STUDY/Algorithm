class Solution{
    public int solution(int N){
        int one_cnt = 0; // 변환된 이진수에서 1 count
        int zero_cnt = 0; // binary gap 판단을 위해 0 count하기 위한 변수
        int long_gap = 0; // 가장 긴 binary gap 값을 저장하기 위한 변수
        String strN = Integer.toBinaryString(N); // 매개변수 N을 이진수로 변환

        System.out.println("N(정수): " + N);
        System.out.println("N(이진수): " + strN);

        // 이진수에 1값이 얼마나 있는지 알아보기 위한 반복문
        for(int i = 0, len = strN.length() ; i < len; i++){
            if(strN.charAt(i) == '1')
                one_cnt++;
        }

        // 이진수에서 1값이 처음으로 등장하는 index를 구함
        int index = strN.indexOf("1");

        // 이진수에서 1값이 없거나 1이 1개만 있는 경우 프로그램 종료(binary gap이 없는 경우)
        if(index == -1 || one_cnt == 1){
            return 0;
        }

        one_cnt--;

        //최초로 1이 나온 것 다음 index부터 검사
        for(int i = index + 1, len = strN.length(); i < len; i++){
            if(strN.charAt(i) == '0'){ // 현재 index의 값이 0이라면
                zero_cnt++; // 0의 개수 누적시킴

            }
            else if(strN.charAt(i) == '1'){ // 현재 index의 값이 1이라면
                if(long_gap <= zero_cnt){ // long_gap 변수값보다 지금 누적한 binary gap값이 크다면
                    long_gap = zero_cnt; // longest binary gap value 갱신
                    zero_cnt = 0; // 다시 세기 위해 zero_cnt값 초기화
                }
                one_cnt--;
                if(one_cnt == 0){ // 이진수에 1이 더이상 없으면 반복문 종료
                    break;
                }
            }
        } // end of for loop

        return long_gap;

    } // end of solution()
} // end of class Solution

class pul8219 {
    public static void main(String[] args){
        Solution s = new Solution();
        int long_gap = 0;
        long_gap = s.solution(529);
        System.out.println("Longest binary gap: " + long_gap);

    } // end of main()

} // end of class pul8219
