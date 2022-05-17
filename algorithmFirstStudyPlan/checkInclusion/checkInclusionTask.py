class Solution:
    def matches(self, hash1: list, hash2: list) -> bool:
        for i in range(26):
            if hash1[i] != hash2[i]: return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1hash = [0 for i in range(26)]
        s2hash = [0 for i in range(26)]

        s1_len = len(s1)
        s2_len = len(s2)
        for i in range(s1_len):
            s1hash[ord(s1[i]) - ord('a')] += 1  # ord - ascii код символа
            s2hash[ord(s2[i]) - ord('a')] += 1

        for i in range(s2_len - s1_len):
            if Solution.matches(self, s1hash, s2hash):
                return True
            s2hash[ord(s2[s1_len + i]) - ord('a')] += 1
            s2hash[ord(s2[i]) - ord('a')] -= 1

        return Solution.matches(self, s1hash, s2hash)


x = Solution()

ans = x.checkInclusion("ab", "eidbaooo")
print(ans)

ans = x.checkInclusion("ab", "eidboaoo")
print(ans)