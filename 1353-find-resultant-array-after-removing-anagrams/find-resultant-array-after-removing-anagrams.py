class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        st= []
        for i in words:
            if st:
                if sorted(st[-1])!=sorted(i):
                    st.append(i)
            else:
                st.append(i)
        return st
