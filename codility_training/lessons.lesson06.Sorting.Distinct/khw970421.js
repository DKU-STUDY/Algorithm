//정확성은 되나 효율성이 안좋다
function solution(A) {
    let p =A.reduce(function(a,b){if(a.indexOf(b)<0)a.push(b);return a;},[]);
    return p.length;
}

//set을 쓰면 strong set에의해 쉽게 distinct 가능
//정확성,효율성 문제x
function solution2 (A) {
    return new Set(A).size
}