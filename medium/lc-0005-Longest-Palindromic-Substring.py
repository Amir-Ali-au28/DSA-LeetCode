def longestPalindrome(s):
    result = ""       
    resLen = 0
    
    for i in range(len(s)):
        
        # ODD LENGTH
        left = i
        right = i
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right-left+1) > resLen:
                result = s[left:right+1]
                resLen = right - left + 1
            left -= 1
            right += 1
            
        # EVEN LENGTH
        left = i
        right = i + 1
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left+1) > resLen:
                result = s[left:right+1]
                resLen = right - left + 1
            left -= 1
            right += 1
            
        return result

s = "babad"
print(longestPalindrome(s))

