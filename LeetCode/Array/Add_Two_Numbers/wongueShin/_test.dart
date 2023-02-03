//import 'package:flutter_test/flutter_test.dart';
import './solution.dart';

List<int> _setUpTest(List<int> nums, int target) {
  final solution = Solution();
  return solution.twoSum(nums, target);
}
/*
TEST_CODE

void main() {
  test(
    "case01",
    () => expect(
      _setUpTest([2, 7, 11, 15], 9),
      equals([0, 1]),
    ),
  );

  test(
    "case02",
    () => expect(
      _setUpTest([3, 2, 4], 6),
      equals([1, 2]),
    ),
  );

  test(
    "case03",
    () => expect(
      _setUpTest([3, 3], 6),
      equals([0, 1]),
    ),
  );
}
 */
