//효율성문제 발생 (for문안에 split,join을 사용해서일듯)
function solution(s){
    let a,b;
    const s_length= s.length;
    for(let i=s.indexOf('()');i<s_length;i++){
        if(s[0]==')'||s[s.length-1]=='(')
            return false;
        s=s.split('()').join('');
        if(s.length==0)
            return true;
    }
    return false;
}

//효율성문제 발생 (for문안에 replace가 있어서 그런듯)
function solution(s){
    const s_length = s.length
    for(let i=0;i<s_length;i++){
        if(s[0]==')'||s[s.length-1]=='(')
            return false;
        s=s.replace(/\(\)/g,'');
    }
    return s.length>0 ? false :true
}


//정확성+효율성 =100
// ()가 묶이려면 기본적으로 왼쪽에서부터 오른쪽으로 진행할때 )의 갯수가 (갯수보다 많으면 ()묶여 처리가 불가능
// 위에 의미는  )가 나오면 1감소 (가 나오면 1증가 할때 총합이 0보다 작아지면  ()묶여 처리 불가능
// 좀 더 map같은 함수를 써보고 싶은데 if else와 더불어 반복문을 줄이기 위해 if가 더있어서 map으로 바꾸기 골치아프다
// (문제 효율성이 좀 이상한지 enter가 하나 더 있는곳은 효율성 문제없고 enter가 하나 없으면 효율성 문제 뜨고 좀 이상하다)

function solution(s){
    const s_length = s.length;
    let answer=0;
    s=s.split('');
    for(let i=0;i<s_length;i++){

        if(s[i]==')')
            answer--;
        else
            answer++;
        if(answer<0)
            return false;
    }

    return answer>0 ? false: true;  //return answer === 0;
}
//출처 : https://programmers.co.kr/learn/courses/30/lessons/12909
