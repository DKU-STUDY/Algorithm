/**
 * https://leetcode.com/problems/minimum-size-subarray-sum/
 * @param s, 양의 정수 s
 * @param nums, 양의 정수 배열
 * @return 연속되는 서브배열의 원소의 합이 s 이상인 배열의 최소 크기
 * 합이 s 이상인 서브 배열이 없으면 0 을 리턴한다.
 */

// 내 솔루션 	204 ms	40.2 MB
// better brute force
const getPrefixSum = (originArr) => {
  return originArr.reduce((prefixSum, num, key) => {
    prefixSum.push((num + prefixSum[key]));
    return prefixSum;
  }, [0]);
};

const minSubArrayLen = function(s, nums) {
  const prefixSum = getPrefixSum(nums);
  let min = Infinity;
  const prefixSumLength = prefixSum.length;

  prefixSum.forEach((sum, key) => {
    for (let j = key + 1 ; j < prefixSumLength ; j++) {
      if ((prefixSum[j] - sum) >= s) {
        min = Math.min(min, j - key);
        break;
      }
    }
  });
  return min === Infinity ? 0 : min;
};

// Brute Force
const minSubArrayLen2 = function(s, nums) {
  const n = nums.length;
  let ans = Infinity;
  for (let i = 0 ; i < n ; i++) {
    for (let j = i ; j < n ; j++) {
      let sum = 0;
      for (let k = i ; k <= j ; k++) {
        sum += nums[k];
      }
      if (sum >= s) {
        ans = min(ans, (j - i + 1));
        break; //Found the smallest subarray with sum>=s starting with index i, hence move to next index
      }
    }
  }
  return (ans != Infinity) ? ans : 0;
};

// Using Binary search 88 ms	41.1 MB
/*
 https://blockdmask.tistory.com/168
 leetcode 의 C++ lower_bound 란?
 - 이진탐색(Binary Search)기반의 탐색 방법입니다. (배열 또는 리스트가 정렬 되어있어야 한다.)
 - @return 찾으려 하는 key 값이 "없으면" key 값보다 큰, 가장 작은 정수 값을 찾습니다.
 - 같은 원소가 여러개 있어도 상관 없으며, 항상 유일한 해를 구할 수 있습니다.
 - 구간이 [start, end]인 배열이 있을때, 중간위치의 index 를 mid 라고 하면,
 arr[mid-1] < key 이면서 arr[mid] >= key 인 최소의 m 값을 찾으면 됩니다. (m>=2)
 */
const lowerBound = (arr, key) => {
  let [start, end, mid] = [0, arr.length, arr.length];

  while (end - start > 0) {     // start 가 end 와 같지 않고, 넘지 않을 때
    mid = ~~((start + end) / 2);    //중앙 index
    (arr[mid] < key) ? (start = mid + 1) : (end = mid);
  }
  return end + 1;
};

const minSubArrayLen3 = function(s, nums) {
  const n = nums.length;
  let ans = Infinity;

  if (n === 0) return 0;

  const prefixSum = getPrefixSum(nums);
  const end = prefixSum.length + 1;

  prefixSum.forEach((sum, key) => {
    if (key === 0 || key === n) return;
    const to_find = s + prefixSum[key - 1];
    const bound = lowerBound(prefixSum, to_find);
    if (bound !== end) {
      ans = Math.min(ans, bound - (key));
    }
  });
  return (ans != Infinity) ? ans : 0;
};


//  Using 2 pointers 64 ms	39.4 MB
const minSubArrayLen4 = function(s, nums) {
  let ans = Infinity;
  let left = 0;
  let sum = 0;

  nums.forEach((num, i) => {
    sum += nums[i];
    while (sum >= s) {
      ans = Math.min(ans, i + 1 - left);
      sum -= nums[left++];
    }
  });
  return (ans != Infinity) ? ans : 0;
};


console.log(minSubArrayLen4(7, [2, 3, 1, 2, 4, 3]) === 2);
console.log(minSubArrayLen4(15, [1, 2, 3, 4, 5]) === 5);
