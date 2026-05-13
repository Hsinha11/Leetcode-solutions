class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        wicket = 0
        for i in events:
            if i.isdigit():
                score+=eval(i)
            elif i=='W':
                wicket+=1
            elif i=="WD" or i=='NB':
                score+=1
            if wicket==10:
                break
        return [score,wicket]