function solution(s) {
    const split =s.split('');
    let number=[];
    let answer=[];
    split.forEach(function(e){
        number.push(e.charCodeAt(0))        //문자를 아스키 코드 숫자로 변환
    })
    number.sort((A,B)=>B-A);                //아스키코드 숫자로 정렬
    number.forEach(function(e){
        answer+=String.fromCharCode(e);    //정렬후 다시 문자로 변환
    })
    return answer;
}
//junilwang.js 코드를 본 후 const를 이용해 변수생성할 필요는 없구나 s.split('') === [...s]
function solution(s) {

    let number=[];
    let answer=[];
    [...s].forEach(function(e){
        number.push(e.charCodeAt(0))        //문자를 아스키 코드 숫자로 변환
    })
    number.sort((A,B)=>B-A);                //아스키코드 숫자로 정렬
    number.forEach(function(e){
        answer+=String.fromCharCode(e);    //정렬후 다시 문자로 변환
    })
    return answer;
}

//junilwang.js 코드를 본 후

function solution (s) {
    return [ ...s ].sort((a, b) => a < b ? 1 : -1).join('');
}
/*
[..s]로 전부 배열에 문자열을 분리시킨 후 sort를 이용해 a<b 비교해서 맞으면(1) 서로 위치 바꾸고 아니라면(-1) 그대로 위치를 둔다
그 후 그것들을 join으로 전부 합친다.
 */
