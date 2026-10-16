def randsom(s1,s2):
    char_count={}
    
    for ch in s1:
        char_count[ch]=char_count.get(ch,0)+1
        
    for ch in s2:
        if ch in char_count:
            char_count[ch]=char_count[ch]-1
            
    for c in char_count.values():
        if c>0:
            return False 
        
    return True 


print(randsom("aab","aacb"))
