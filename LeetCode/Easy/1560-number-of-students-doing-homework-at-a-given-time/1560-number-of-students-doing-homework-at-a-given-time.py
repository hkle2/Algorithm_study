class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                answer += 1
        return answer

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime and e >= queryTime:
                answer += 1
        return answer