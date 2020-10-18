function solution(x) {
    return (x%String(x).split('').reduce((a,b)=>Number(a)+Number(b))==0)?(true):false;
}

//  출처 : https://programmers.co.kr/learn/courses/30/lessons/12947
