// Brute Force
const myTwoSum = function(nums, target) {
  const len = nums.length;
  for(let i = 0; i < len ; i++){
    for (let j = i + 1; j < len; j++) {
      if ((nums[i] + nums[j]) === target) return [i, j];
    }
  }
};


// Two-pass Hash Table
const twoSum2 = function(nums, target) {
  const hash = {};
  const len = nums.length;

  for (let i = 0; i < len; i++)
    hash[nums[i]] =  i;
  for (let i = 0; i < len; i++) {
    const complement = target - nums[i];
    const hashValue = hash[complement];
    if (hashValue && hashValue != i)
      return [i, hashValue];
  }
};

// One-pass Hash Table
const twoSum = function(nums, target) {
  const hash = {};
  const len = nums.length;

  for (let i = 0; i < len; i++) {
    const thisNum = nums[i];
    const complement = target - thisNum;
    const hashValue = hash[complement];

    if (hashValue !== undefined)
      return [hashValue, i];
    hash[thisNum] = i;
  }
};


console.log(
  twoSum([2,7,11,15], 9),
  // [0, 1]
  twoSum([3,2,4], 6),
  // [1, 2]
  twoSum([3,3], 6)
  // [1,0]
)