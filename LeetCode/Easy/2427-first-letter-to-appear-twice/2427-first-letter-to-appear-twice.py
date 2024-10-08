from collections import defaultdict

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
            if d[c] > 1:
                return c

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()
        for c in s:
            if c in visited:
                return c
            visited.add(c)

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = []
        for i in range(len(s)):
            if s[i] in visited:
                return s[i]
            visited.append(s[i])