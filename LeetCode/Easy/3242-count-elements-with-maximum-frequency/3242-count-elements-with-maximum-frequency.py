from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        answer = 0
        m = max(nums_counter.values())
        for k, v in nums_counter.items():
            if v == m:
                answer += v
        return answer

from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        answer = 0
        nums_dict = Counter(nums)
        for i, j in nums_dict.items():
            if j == max(nums_dict.values()):
                answer += j
        return answer