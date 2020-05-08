
function solution(A) {
    const set = Array.from(new Set(A));
    return set.length;
}
solution([2,1,1,2,3,1]);