/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} target
 * @return {number[][]}
 */


const pathSum = function (root, target) {
    const answer = [];
    dfs(root, [], 0, answer, target);
    return answer;
};

function dfs(node, route, sum, answer, target) {
    if (!node)
        return;

    const val = node.val;

    if (!node.right && !node.left)
        return sum + val === target ? answer.push([...route, val]) : null;

    if (node.right)
        dfs(node.right, [...route, val], sum + val, answer, target);

    if (node.left)
        dfs(node.left, [...route, val], sum + val, answer, target);
}