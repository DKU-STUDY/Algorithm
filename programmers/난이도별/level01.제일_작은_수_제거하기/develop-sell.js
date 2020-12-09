function solution(arr) {
    let answer = [];
    let len = arr.length
    let min = Number.MAX_VALUE;
    let index = 0;
    arr.forEach(function(e, i){
        if(min > e){
            min = e;
            index = i;
        }
    })
    arr.splice(index, 1)
    return len === 1 ? [-1] : arr;
}

// 문제풀이:
// 예전에 처음 프로그래밍 배울 때 풀던 문제 같다
// min값을 갖고 있는 index를 구하고,
// 그 위치의 요소를 찾아 없애는 방식이다.

// 한줄 풀이:
// arr.splice(arr.indexOf(Math.min(...arr)),1);

// Math.min 이라는 함수로 최소값을 구할 수 있고, 
// 이때 배열을 ... 로 빼낸 다음 실행해야 가능하다.
// indexOf 함수로 해당 값을 찾아서 splice로 값을 없애준다. (min에 해당되는 index를 구하는 작업이 불필요)
