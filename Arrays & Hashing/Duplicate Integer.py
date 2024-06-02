class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        H = set()
        for i in nums:
            if i in H:
                return True
            H.add(i)
        return False
          