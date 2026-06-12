class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        left = 0
        max_frequent_letter_count = 0 
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequent_letter_count = max(max_frequent_letter_count, count[s[right]])
            letters_to_replace = (right - left + 1) - max_frequent_letter_count
            if letters_to_replace > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)  
        return longest