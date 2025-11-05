class Solution:
    def findPoisonedDuration(self, time: List[int], duration: int) -> int:
        ans=0
        for i in range(1,len(time)):
            if (time[i]-time[i-1])<duration:
                ans+=time[i]-time[i-1]
            else:
                ans+=duration
        ans+=duration
        return ans