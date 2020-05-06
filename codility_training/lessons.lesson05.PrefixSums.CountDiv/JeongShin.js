/*처음 작성한 코드*/
function solution(A, B, K) {
    // A랑 가장 가까운 범위 내 숫자
    const start = A % K ? A + K - A % K : A;
    // B랑 가장 가까운 범위 내 숫자
    const end = B - B % K;
    if (end >= start)
        return (end - start) / K + 1;
    else
        return 0;
}

/*@eyabc 님 코드보고 훨씬 가독성도 좋고 효율적인거 같아서 다시 작성해보았습니다.*/
//
function solution2(A, B, K) {
    // B까지 총 K 배수의 개수
    const rear = Math.floor(B / K);
    const front = Math.floor(A / K) - (A % K ? 0 : 1);
    return (Math.floor(B / K) - Math.floor(A / K) - (A % K ? 0 : 1));
    // 이렇게 하면 왜 아예 다른 결과가 나오는지 잘 모르겠네요 ㅠ
    // return rear - front;
}

function solution3(A, B, K) {
    if (A === B) return B % K === 0 ? 1 : 0;
    return ~~(B / K) - ~~(A / K) - (A % K ? 0 : 1);
}

console.log(solution3(3, 10, 4));