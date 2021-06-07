package LeetCode.String.ZigZag_Conversion;

public class Seokbin {
	public String convert(String s, int numRows) {

		char[] chars = s.toCharArray();
		int idx = 0;
		// StringBuffer sb = new StringBuffer(numRows);
		// 스트링버퍼 배열로 선언!!
		StringBuffer[] sb = new StringBuffer[numRows];
		// 배열에 스트링 버퍼 각각 저장
		for (int i = 0; i < numRows; i++) {
			sb[i] = new StringBuffer();
		}

		while (idx < s.length()) {
			// 수직으로 내려갈 때
			for (int i = 0; i < numRows && idx < s.length(); i++) {
				sb[i].append(chars[idx++]);
			}
			// 대각선으로 올라갈 때
			for (int i = numRows - 2; i > 0 && idx < s.length(); i--) {
				sb[i].append(chars[idx++]);
			}

		}
		//스트링 버퍼 합치기
		for (int i = 1; i < numRows; i++) {
			sb[0].append(sb[i]);
		}
		String answer = new String(sb[0]);
		return answer;
	}
}
