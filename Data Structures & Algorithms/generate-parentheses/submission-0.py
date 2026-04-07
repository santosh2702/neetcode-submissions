class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(cur, start, end):
            if len(cur) == 2*n:
                res.append(cur)
                return

            if start < n:
                backtrack(cur + "(", start+1, end)
            if end < start:
                backtrack(cur + ")", start, end+1)
        backtrack("",0,0)
        return res