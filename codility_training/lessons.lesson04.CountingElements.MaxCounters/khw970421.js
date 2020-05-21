function solution(N, A) {
    let arrNumber = new Array(); //배열선언
    let max=0;
    for(let i=0;i<N;i++){
        arrNumber[i]=0;
    }
    A.reduce(function(acc,value){
        if(value>N){
            arrNumber.fill(max);
        }
        else{
            arrNumber[value-1]++;
            max=Math.max(arrNumber[value-1],max);
        }
    },0);
    return arrNumber;
}

console.log(solution(5, [3, 4, 4, 6, 1, 4, 4]).toString()=== [3, 2, 2, 4, 2].toString());