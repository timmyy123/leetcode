class Solution:
    def checkDivider(self, a,b):
        if len(a)<len(b):
            return self.checkDivider(b,a)
        return len(a)%len(b) == 0 and a == b*(len(a)//len(b))
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        if self.checkDivider(str1, str2):
            return str2
        for i in [cdl for cdl in range(1,(len(str2)//2)+1) if len(str1)%cdl == 0 and len(str2)%cdl == 0][::-1]:
            if self.checkDivider(str2, str2[0: i]) and self.checkDivider(str1, str2[0: i]):
                return str2[:i]
        return ''
        