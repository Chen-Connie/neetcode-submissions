from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      counts = Counter(nums)
      for key, value  in counts.items():
        if value > 1:
            return True
        
      return False
    