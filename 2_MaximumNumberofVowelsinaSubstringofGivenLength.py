class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        max_count = -1
        count = 0

        for i,ch in enumerate(s):
            end = i + k - 1
            st = i
            if end < len(s):
                if i==0:
                    while st<=end:
                        if s[st] in vowels:
                            count+=1
                        st+=1

                else:
                    if s[st-1] in vowels:
                        count-=1
                    if s[end] in vowels:
                        count+=1
                max_count = max(max_count,count)
                if max_count==k:
                    break
        return max_count
