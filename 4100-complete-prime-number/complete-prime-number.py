class Solution:
    def is_prime(self,n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    def completePrime(self, num: int) -> bool:
        pre = []
        suf = []
        nums = str(num)
        for i in range(len(nums)):
            # print(nums[:i+1])
            pre.append(int(nums[:i+1]))
        for i in range(1, len(nums)+1):
            # print(nums[-i:])
            suf.append(int(nums[-i:]))
        for i in range(len(pre)):
            pre[i] = self.is_prime(pre[i])
        for i in range(len(suf)):
            suf[i] = self.is_prime(suf[i])
        return all(pre) and all(suf)
