class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, node):
            if i == len(nums):
                res.append(node[:])
                return
            
            node.append(nums[i])
            dfs(i+1, node)
            node.pop()
            dfs(i+1, node)

        dfs(0, [])
        return res
