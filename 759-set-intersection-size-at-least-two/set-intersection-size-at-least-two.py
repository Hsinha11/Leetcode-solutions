class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[1], -x[0]))
        c=0
        p1 = intervals[0][-1]-1
        p2 = intervals[0][-1]
        # print(p1,p2)
        c=2
        if len(intervals)>1:
            for i in intervals[1:]:
                start,end = i
                if start>p2:
                    c+=2
                    p1 = end-1
                    p2 =end
                elif start>p1:
                    c+=1
                    p1 = p2
                    p2 = end
                else:
                    continue
        return c