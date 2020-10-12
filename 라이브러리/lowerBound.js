const lowerBound = (arr, key) => {
  let [start, end, mid] = [0, arr.length, arr.length];

  while (end - start > 0) {     // start 가 end 와 같지 않고, 넘지 않을 때
    mid = ~~((start + end) / 2);    //중앙 index
    (arr[mid] < key) ? (start = mid + 1) : (end = mid);
  }
  return end + 1;
};
/*
 https://blockdmask.tistory.com/168
 C++ lower_bound 란?
 - 이진탐색(Binary Search)기반의 탐색 방법입니다. (배열 또는 리스트가 정렬 되어있어야 한다.)
 - @return 찾으려 하는 key 값이 "없으면" key 값보다 큰, 가장 작은 정수 값을 찾습니다.
 - 같은 원소가 여러개 있어도 상관 없으며, 항상 유일한 해를 구할 수 있습니다.
 - 구간이 [start, end]인 배열이 있을때, 중간위치의 index 를 mid 라고 하면,
 arr[mid-1] < key 이면서 arr[mid] >= key 인 최소의 m 값을 찾으면 됩니다. (m>=2)
 */