class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pairs = []
        def generatePairs(li):
            if sum(li) == n:
                zeros = 2*n - len(li)
                pair = li
                for z in range(zeros):
                    pair.append(0)
                pairs.append(pair)
            else:
                generatePairs(li+[1])
                if sum(li)*2 > len(li):
                    generatePairs(li+[0])
        generatePairs([1])
        return [ ''.join(['(' if i == 1 else ')' for i in pair]) for pair in pairs]

        