function solution(s) {
    let h =s.split(' ');        //공백에따라 분리하기
    const p=[];
    const q = [];
    const h_length=h.length;

    for(let i=0;i<h_length;i++)
        p[i]= h[i].split('');   //공백에 따라 분리한것을 다시 글자마다 분리하기

    const p_length = p.length;

    for(let i=0;i<p_length;i++)
    {
        for(let j=0;j<p[i].length;j++)
        {
            if(j%2==0)
                q.push(p[i][j].toUpperCase())   //공백에따라 나눈 글자단위 기준으로 짝수이면 대문자로
            else
                q.push(p[i][j].toLowerCase());  //홀수이면 소문자로
        }
        q.push(' ') //공백도 포함
    }
    q.pop();    //맨 마지막에도 공백이 포함되니 그건 지우기

    return q.join('');
}


//준일이형 피드백으로 수정

function solution(s) {
    return s.toUpperCase().split(' ').map(e=>e.split('').map((q,k)=>(k%2==1)?q.toLowerCase():q).join('')).join(' ')
}

//map을 마치 for문으로 생각하면 map안에 map이 있으므로 이중 for문에 대해 안에서 처리하고 join 후 밖의 map에서 다시 배열을 join
