function solution(x) {
    return (x%String(x).split('').reduce((a,b)=>Number(a)+Number(b))==0)?(true):false;
}

//  출처 : https://programmers.co.kr/learn/courses/30/lessons/12947

//수정한 코드 (가독성 높이기위해)

function solution(x) {
    return (x%number_Of_Digits(x)==0)?(true):false;
}

function number_Of_Digits(x){       //자릿수에 따라 더한값을 return
    return  String(x).split('').reduce((a,b)=>Number(a)+Number(b));
}
