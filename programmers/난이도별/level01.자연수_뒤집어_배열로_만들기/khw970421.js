function solution(n) {
    let answer = [];
    let swap=0;

    answer.push(String(n));
    let h =answer[0].split('');     //숫자를 전부 한글자씩 배열에 분리
    const h_length = h.length;

    for(let i=0;i<h_length/2;i++)
    {       swap=h[i];
        h[i]=h[h.length-1-i];
        h[h.length-1-i]=swap;          //배열로 나열한 것을 뒤집어 나타내기
    }

    for(let i=0;i<h_length;i++)
        h[i]=Number(h[i]);      //뒤집어 나타내는것을 문자에서 숫자로 변환
    return h;
}

//좀더 간단히 만든 코드
function solution(n) {
    let answer = [];
    answer.push(String(n));
    return answer[0].split('').reverse().map(x=>Number(x));
    //문자를 글자마다 분리하고 위치를 뒤집은 후 문자를 숫자로 변환후 반환
}

// 더 간단히 만들기
function solution(n)
{
    return n.toString().split('').reverse().map(x=>Number(x));
}

