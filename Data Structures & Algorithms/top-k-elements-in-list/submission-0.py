class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        a = []
        count = Counter(nums)

        for i in range(k):
            for key, value in count.items():
                if value == max(count.values()):
                    a.append(key)
                    break

            count.pop(key)

        return a


        