// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
     const size = A.length;   
     var mySet = new Set();
      for(let i=0;i<size;i++)             //크기만큼 반복
    {       
        if(mySet.has(A[i])==false)mySet.add(A[i]);
        else mySet.delete(A[i]);
    }
    console.log(mySet);
    return mySet[0];
}


Example test:   [9, 3, 9, 3, 9, 7, 9]
Output (stderr):
Invalid result type, integer expected, 'undefined' found
Perhaps you are missing a 'return'?
Output:
Set { 7 }
RUNTIME ERROR (tested program terminated with exit code 1)

원하는 Set의 남은 한가지를 찾긴했는데 return 부분에서 어떻게 mySet부분의 저걸 return 해야 하는지 잘 모르겠어서여
