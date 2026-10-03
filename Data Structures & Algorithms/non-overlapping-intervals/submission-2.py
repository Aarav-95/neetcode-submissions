class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals) 
        count = 0  
        i = 0
        cur = intervals[0] 
        while i < len(intervals)-1:
            if intervals[i+1][0] >= cur[1]:
                cur = intervals[i+1]
            else:
                if cur[1] > intervals[i+1][1]:
                    cur = intervals[i+1]
                count += 1
            i += 1
        
        return count