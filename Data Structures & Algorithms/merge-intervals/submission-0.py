class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        i = 0
        cur = [intervals[0][0], intervals[0][1]]
        while i < len(intervals)-1:
            if intervals[i+1][0] > cur[1]:
                res.append(cur)
                cur = intervals[i+1]
            else:
                cur = [min(cur[0], intervals[i+1][0]), max(cur[1], intervals[i+1][1])]
            i += 1

        res.append(cur)
        return res 
        
