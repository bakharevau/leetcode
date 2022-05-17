class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ''
        maximum = 0
        for letter in s:
            if letter not in seen:
                seen += letter
            else:
                seen = seen[seen.index(letter)+1:]+letter #начинаем "смотреть" от повторяющейся буквы
            maximum = max(maximum, len(seen))
        return maximum

#idea from: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/389496/Python-easy-solution-with-comment-90-O(n)-speed-and-98-space


x = Solution()
# ans = x.lengthOfLongestSubstring("pwwkew")
# print(ans)
#
# ans = x.lengthOfLongestSubstring("gaaqfeqlqky")
# print(ans)

ans = x.lengthOfLongestSubstring("dvdf")
print(ans)

ans = x.lengthOfLongestSubstring("bbbbb")
print(ans)

ans = x.lengthOfLongestSubstring("asljlj")
print(ans)

ans = x.lengthOfLongestSubstring("hdgikkinyyzxycsekxoev")
print(ans)
