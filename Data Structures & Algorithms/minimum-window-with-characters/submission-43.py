class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if m == 0 or n < m:
            return ""
        sc = list(map(ord, s))
        tc = list(map(ord, t))
        need = [0] * (max(max(sc), max(tc)) + 1)
        for c in tc:
            need[c] += 1
        missing = m
        best_len, best_l = n + 1, 0
        l = 0
        for r, c in enumerate(sc):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1                       # negative = surplus / irrelevant
            if missing == 0:
                while need[sc[l]] < 0:         # drop surplus on the left
                    need[sc[l]] += 1
                    l += 1
                if r - l + 1 < best_len:
                    best_len, best_l = r - l + 1, l
                    if best_len == m:          # can't do better than len(t)
                        break
                need[sc[l]] += 1               # drop a required char, resume expanding
                missing += 1
                l += 1
        return "" if best_len > n else s[best_l:best_l + best_len]