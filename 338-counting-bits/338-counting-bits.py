class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for integer in range(0, n+1):
            binary = list((format(integer, "b")))
            binaryInt =  [int(x) for x in binary]
            
            output.append(sum(binaryInt))
        return output
            
            
        