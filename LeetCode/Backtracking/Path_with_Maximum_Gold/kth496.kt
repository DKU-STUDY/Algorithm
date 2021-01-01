import kotlin.math.max

class Solution {

    fun getMaximumGold(grid: Array<IntArray>): Int {
        val R = grid.size; val C = grid[0].size
        val dr: IntArray = intArrayOf(0, 0, 1, -1)
        val dc: IntArray = intArrayOf(1, -1, 0, 0)
        var answer = 0
        val visited: Array<BooleanArray> = Array(R) { BooleanArray(C) { false } }

        fun dfs(r: Int, c: Int, acc: Int) {
            visited[r][c] = true
            val ret = acc + grid[r][c]
            var flag = false
            for (i in 0..3) {
                val nr = r + dr[i]
                val nc = c + dc[i]
                if (nr in 0 until R && nc in 0 until C && !visited[nr][nc] && grid[nr][nc] > 0) {
                    flag = true
                    dfs(nr, nc, ret)
                }
            }
            if (!flag) answer = max(answer, ret)
            visited[r][c] = false
        }

        for (r in 0 until R) {
            for (c in 0 until C) {
                if (grid[r][c] > 0) {
                    dfs(r, c, 0)
                }
            }
        }

        return answer
    }
}