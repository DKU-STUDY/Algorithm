/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} root
 * @param {number} sum
 * @return {number}
 */
const pathSum = function (root, sum) {
  const memo = { 0: 1 };
  const self = this;
  self.answer = 0;
  dfs.call(self, root, sum, 0, memo);
  return self.answer;
};

function dfs(node, target, currSum, memo) {
  if (!node)
    return;

  currSum += node.val;

  this.answer += (memo[currSum - target] || 0);
  memo[currSum] = (memo[currSum] || 0) + 1;

  dfs.call(this, node.left, target, currSum, memo);
  dfs.call(this, node.right, target, currSum, memo);

  memo[currSum]--;
}

