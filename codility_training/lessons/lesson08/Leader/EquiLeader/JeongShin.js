function solution(A) {
    const getLeader = (obj, len) => {
        for (const [key, val] of Object.entries(obj)) {
            if (val > len / 2)
                return key;
        }
        return -1;
    };
    const left = {}, right = {};
    A.forEach(el => right[el] = (right[el] || 0) + 1); //오른쪽 오브젝트에 A 모든 요소 삽입
    let [llen, rlen] = [0, A.length]; // .length 메소드 사용을 줄이기 위한 변수
    if (Object.keys(right).length > rlen / 2) // 숫자가 A 배열 절반 이상으로 다양하면 leader는 존재할 수 없다.    ex) [1,2,2,2,3,5,2,2,7,6]
        return 0;
    return A.reduce((count, el) => {
        --right[el];
        left[el] = (left[el] || 0) + 1;
        const [l, r] = [getLeader(left, ++llen), getLeader(right, --rlen)];
        return count + (l === r && l !== -1)
    }, 0);
}
