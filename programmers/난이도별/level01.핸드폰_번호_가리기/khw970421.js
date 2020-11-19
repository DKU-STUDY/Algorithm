function solution(phone_number) {
    let answer = '',a=[];
    answer = phone_number.split('').splice(phone_number.length-4,4,'*')
    for(let i=0;i<phone_number.length-4;i++)
        a.push('*')
    return a.concat(answer).join('');
}


//수정한 코드

function solution(phone_number) {
    let answer = '';
    answer = phone_number.split('').splice(phone_number.length-4,4,'*')
    return phone_number.slice(0,phone_number.length-4).replace(/[0-9]/g,'*').concat(answer.join(''))
}


//출처 : https://programmers.co.kr/learn/courses/30/lessons/12948
