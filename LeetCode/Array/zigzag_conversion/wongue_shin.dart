/*
Runtime 380 ms
Beats 94.83%
--------------
Memory 160.4 MB
Beats 43.10%
 */

// import 'package:flutter_test/flutter_test.dart';

class Solution {
  late final int _sliceLen;

  String convert(String s, int numRows) {
    // numRows 가 1인경우, 원본 스트링을 그대로 반환하면 된다.
    if (numRows == 1) return s;
    _sliceLen = numRows + (numRows - 2);
    List<List<String>> ans = List.generate(numRows, (index) => []);
    for (int i = 0; i < s.length; i = i + _sliceLen) {
      int endIdx = i + _sliceLen < s.length ? i + _sliceLen : s.length;
      _reorderString(ans, s.substring(i, endIdx), numRows);
    }

    return ans.map((e) => e.join()).join();
  }

  void _reorderString(List<List<String>> ans, String slicedString, int numRows) {
    for (int idx = 0; idx < slicedString.length; idx++) {
      if (idx == 0 || idx == numRows - 1 || idx < numRows) {
        ans[idx].add(slicedString[idx]);
        continue;
      }
      ans[_sliceLen - idx].add(slicedString[idx]);
    }
  }
}

/*
TEST_CODE
--------
void main() {
  group(
    "Zigzag Conversion",
        () {
      late Solution solution;
      setUp(() {
        solution = Solution();
      });

      test('case01', () => expect(solution.convert("PAYPALISHIRING", 3), equals("PAHNAPLSIIGYIR")));
      test('case02', () => expect(solution.convert("PAYPALISHIRING", 4), equals("PINALSIGYAHRPI")));
      test('case03', () => expect(solution.convert("A", 1), equals("A")));
    },
  );
}
*/