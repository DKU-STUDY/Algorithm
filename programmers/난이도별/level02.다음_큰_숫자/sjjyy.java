public class sjjyy {

    /*
    조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
    조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
    조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
     */

    public static int solution(int n) {
        String nToBinary = Integer.toBinaryString(n);
        int nCount = 0;
        // 입력된 값을 이진수로 변환 후 1 개수 카운트
        for(int i=0; i<nToBinary.length(); i++) {
            if(nToBinary.charAt(i) == '1')
                nCount++;
        }

        int tmp = 0, tmpCount = 0;
        for(tmp = n+1; nCount != tmpCount; tmp++) {
            // n의 다음 큰 수 구하기
            String tmpToBinary = Integer.toBinaryString(tmp);
            tmpCount = 0;
            // 구한 값을 이진수로 변환 후 1 개수 카운트
            for(int i=0; i<tmpToBinary.length(); i++) {
                if(tmpToBinary.charAt(i) == '1')
                    tmpCount++;
            }
        }

        return tmp-1;
        // 마지막에 늘어난 tmp 값 빼기
    }

    public static void main(String [] args) {
        System.out.println(solution(78)); // 83 (1010011)
        System.out.println(solution(15)); // 23 (10111)
    }
}
