function solution(nums) {
    const set1 = new Set(nums);
    const n_divide_length = nums.length/2;
    var result = Array.from(set1);
    if(n_divide_length<result.length){
        return n_divide_length;
    }
    else if(n_divide_length>=result.length){
        return result.length;
    }

}

//좀더 간결하고 const 생각하면서 수정
function solution(nums) {
    const set1 = new Set(nums);     //중복된 것을 제거한 set1 설정
    const result = Array.from(set1);    // 다시 set1을 배열로 변환

    const n_divide_length = nums.length/2;  // N/2만큼 가져가도 좋은 크기 설정
    const result_length = result.length;    // 중복을 제외한 가능한 모든 종류의 갯수
    return (n_divide_length<result.length)?n_divide_length:result.length;
    // 가져가도 되는 양이 중복을 제외한 가능한 양보다 적으면 가져가도 되는양만 챙기고 그외에 같거나 많다면 중복을 제외한 가능한 모든 종류의 수를 return
}

//피드백 후 가능한 코드
function solution(nums) {
    const set = new Set(nums);     //중복된 것을 제거한 set1 설정
    const n_divide_length = nums.length / 2;  // N/2만큼 가져가도 좋은 크기 설정
    return Math.min(nums.length / 2, set.size);
}
