function solution(n) {
    return Number(n.toString().split('').map(x=>Number(x)).sort((A,B)=>B-A).join(''));
}
//값을 문자로바꿔 분리시킨후 숫자로 변환후 정렬시키고 다시 합쳐서 Number 형태로 반환
