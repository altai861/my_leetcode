class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
    
testcases = {
    [[1,2],[2,3],[3,4],[1,3]]: 1,
    [[1,2],[1,2],[1,2]]: 2,
    [[1,2],[2,3]]: 0
}

    
solution = Solution()

for case in testcases.keys():
    if solution.eraseOverlapIntervals(case) == testcases[case]:
        print(f'passed\ttest{case}')
    else:
        print(f'failed\ttest{case}')

