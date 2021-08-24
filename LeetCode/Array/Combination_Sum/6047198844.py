class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx: int, acc: int, elements: List):
            # pruning
            if acc > target:
                return

            if idx == len(candidates):
                if target == sum(elements):
                    result.append(elements)
                return

            # 현재 인덱스 선택. 또 선택가능
            dfs(idx, acc + candidates[idx], elements + [candidates[idx]])
            # 현재 인덱스 선택 거부
            dfs(idx + 1, acc, elements)

        result = []
        dfs(0, 0, [])
        return result