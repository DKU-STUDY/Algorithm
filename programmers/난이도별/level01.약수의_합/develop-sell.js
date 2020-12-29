function solution(n) {
  if (n < 2) return n;
  let answer = 0;
  let arr = [];
  let limit = Math.sqrt(n);
  for(let i = 1; i <= limit ; i ++){
      if (n % i === 0){
          if (n / i === i) {
            arr.push(i);
          }
          else{
              arr.push(n / i)
              arr.push(i); 
          }
      }
  }
  answer = arr.reduce((sum, num) => sum + num, 0);
  return answer;
}

// 문제풀이: 
// 약수를 구해서 배열에 넣고 해당 배열의 합을 구하는 식으로 구현했다.

// 지난번 풀었던 문제 중 약수를 구할 때 Math.sqrt()까지 진행해도 약수를 구할 수 있음을 알고
// 이 문제에 적용시켰다. 

// 알게된 점: 
// 배열을 굳이 만들 필요 없이 바로 sum이라는 integer형 변수에 더하면 더 효율적이었을 것 같다. 

// reduce 함수를 통해 배열의 합을 구할 수 있다. 
// arr.reduce((sum, num) => sum + num, 0); => num은 배열 요소, sum은 최종 합 
