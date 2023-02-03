/*
* RunTime 393ms
* 78.54 %
* -------------
* Memory 157.5MB
* 48.85 %
* */
class Solution {
  late final List<int> _num;

  List<int>? _searchFromCurrentIdx(int idx, int target) {
    for (int jdx = idx + 1; jdx < _num.length; jdx++) {
      if (_num[idx] + _num[jdx] == target) {
        //print("[$idx(= ${_num[idx]}), jdx(= ${_num[jdx]})] => ${_num[idx] + _num[jdx]} ");
        return [idx, jdx];
      }
    }
    return null;
  }

  List<int> twoSum(List<int> nums, int target) {
    _num = nums;
    for (int idx = 0; idx < _num.length; idx++) {
      List<int>? possibleAns = _searchFromCurrentIdx(idx, target);
      if (possibleAns != null) {
        return possibleAns;
      }
    }
    return [0, 1]; // 문제의 설명이 정확 하면 (적어도 하나의 해를 가진다면) 도달하지 않는 코드.
  }
}