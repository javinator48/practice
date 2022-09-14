class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokensNew = sorted(tokens)
        print(tokensNew)
        dequeTokens = deque(tokensNew)
        score = 0 
        maxscorevar = 0 
        while(dequeTokens and (power>dequeTokens[0] or score)): 
            
            if (power>=dequeTokens[0]):
                power -= dequeTokens.popleft()
                score += 1 
           
            
            elif score: 
                power += dequeTokens.pop()
                score -= 1 
            maxscorevar = max(score,maxscorevar)
           
        return maxscorevar
                
            
        