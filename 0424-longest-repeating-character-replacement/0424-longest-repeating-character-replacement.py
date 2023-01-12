class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0 
        res = 0 
        
       
        for r in range(len(s)): 
            counts[s[r]] = 1 + counts.get(s[r], 0)

            #the next line doesn't make sense to me 
            
            if (r-l+1) - max(counts.values()) > k: 
                counts[s[l]] -= 1
                l+=1 
            res = max(res, r-l+1)
        return res