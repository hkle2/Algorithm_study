class Solution:
    def minimumChairs(self, s: str) -> int:
        answer = 0
        cnt = 0
        for c in s:
            if c == "E":
                cnt += 1
            else:
                cnt -= 1
            answer = max(cnt, answer)
        return answer

class Solution:
    def minimumChairs(self, s: str) -> int:
        chair = 0
        answer = 0
        for i in range(len(s)):
            if s[i] == "E":
                chair += 1
                if answer < chair:
                    answer = chair
            else:
                chair -= 1
        return answer