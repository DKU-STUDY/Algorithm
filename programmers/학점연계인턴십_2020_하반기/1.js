/*
* 반에 아이들의 키가 다음과 같을때
* height = [1, 1, 3, 3, 4, 1]
* 키 순으로 정렬하여 원래 배열과 비교 했을때
* 제자리에 서있지 않은 학생의 수를 반환하는 문제
* [1, 1, 3, 3, 4, 1] => [1, 1, 1, 3, 3, 4] 3을 반환 해야함
*/
function countStudents(height) {
    const sorted = [...height].sort((a, b) => a - b);
    return sorted.reduce((acc, curr, idx) => acc + (curr !== height[idx]), 0)
}