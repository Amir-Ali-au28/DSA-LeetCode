def countSubstrings(s):
    result = 0
    
    for i in range(len(s)):
        left = i
        right = i
        while left >=0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
            
        left = i
        right = i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right += 1
    return result

s = "aaa"
print(countSubstrings(s))



# Bruteforce approch. Taking O(n^3) time complexity.

def countSubstrings1(self, s: str) -> int:
    result = 0
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = s[i:j+1]
            if temp == temp[::-1]:
                result += 1
                
    return result

