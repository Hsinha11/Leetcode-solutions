class Solution:
    def smallestNumber(self, pattern: str) -> str:
        st= []
        res = ''
        n = len(pattern)
        for i in range(n+1):
            st.append(i+1)
            if i==n or pattern[i]=='I':
                while st:
                    res+=str(st.pop(-1))
            # elif pattern[i]=='D':
        return res
                # st.append()