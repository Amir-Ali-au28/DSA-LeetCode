def isIsomorphic(s, t):
    hashMapS = {}
    hashMapT = {}
    
    for i in range(len(s)):
        if s[i] not in hashMapS:
            hashMapS[s[i]] = t[i]
        else:
            if hashMapS[s[i]] != t[i]:
                return False
            
        if t[i] not in hashMapT:
            hashMapT[t[i]] = s[i]
        else:
            if hashMapT[t[i]] != s[i]:
                return False
        
    return True

s = "egg"
t = "add"

print(isIsomorphic(s,t))

