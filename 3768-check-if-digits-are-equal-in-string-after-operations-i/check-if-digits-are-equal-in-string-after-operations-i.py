class Solution:
    def hasSameDigits(self, s: str) -> bool:
        temp = ''
        while len(s)!=2:
            for i in range(len(s)-1):
                val = (int(s[i])+int(s[i+1]))%10
                temp+=str(val)
            s=temp
            temp=''
            # print(s)    
        return s[0]==s[1]