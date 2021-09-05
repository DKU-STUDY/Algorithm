class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # IP길이가 4개~12개사이여야한다.
        if not (4 <= len(s) <= 12):
            return []
        res = []
        for i in product([1, 2, 3], repeat=4):
            if sum(i) == len(s):
                IP = ''
                pointer = 0
                for j in i:
                    k = s[pointer:pointer + j]
                    if 0 <= int(k) <= 255:
                        IP += '.' + str(int(k))
                        pointer += j
                    else:
                        break
                else:
                    if len(IP) == len(s) + 4:
                        res.append(IP[1:])
        return res
