class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ans = ''
        for word in words:
            n = len(word)
            ans += ''.join([word[n - i - 1] for i in range(len(word))]) + ' '
        return ans.strip()

x = Solution()
ans = x.reverseWords("Let's take LeetCode contest")
print(ans)

ans = x.reverseWords("God Ding")
print(ans)
