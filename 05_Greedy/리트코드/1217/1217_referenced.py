# 1217. referenced code
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even= sum(chip%2 for chip in chips)
        return min(even, len(chips)-even)
        
