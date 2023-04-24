#Leet Code # 424
#RunTime = O(26*n) = O(n)
#SpaceComplexity = O(26)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashCount = {}
        result = 0
        lptr = 0

        for rptr in range(len(s)):
            hashCount[s[rptr]] = 1 + hashCount.get(s[rptr], 0)
            while (rptr - lptr + 1) - max(hashCount.values()) > k:
                hashCount[s[lptr]] -= 1
                lptr += 1
            
            result = max(result, rptr-lptr+1)
        
        return result
