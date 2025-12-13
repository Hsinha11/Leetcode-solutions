class Solution:
    def groupThePeople(self, group: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(group)):
            d[group[i]].append(i)
        # print(d)
        l =[]
        for i in d:
            for j in range(0,len(d[i]),i):
                l.append(d[i][j:j+i])
        return l
        