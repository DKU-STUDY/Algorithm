class Solution:
    def defangIPaddr(self, address: str) -> str:
        for _ in range(3):
            address = address.replace(".","[.]")
        return address