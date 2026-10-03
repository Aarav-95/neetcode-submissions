class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}

        for i in hand:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        hand = sorted(hand)

        for i in hand:
            if freq[i] > 0:
                for j in range(groupSize):
                    if i+j in freq:
                        freq[i+j] -= 1
                    else:
                        return False
        
        return True
                    

        
