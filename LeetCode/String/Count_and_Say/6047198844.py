class Solution:
    def countAndSay(self, n: int) -> str:
        def say(cnt, s):
            if cnt == n + 1:
                return s

            res = ""
            if cnt == 1:
                res = "1"
            else:
                # 앞에서부터 count한다.
                cur = ""
                cur_cnt = 0

                for char in s:
                    if cur == char:
                        cur_cnt += 1
                    else:
                        if cur_cnt != 0:
                            res += str(cur_cnt) + cur
                        cur = char
                        cur_cnt = 1

                res += str(cur_cnt) + cur

            return say(cnt + 1, res)

        return say(1, "")