x#suppose we have 2 strings , s1="aab". s2="aacb" , return true if s1 can be created by s2.

def randsom(s1,s2):
    dict={}
    sec_dict={}
    if len(s2)<len(s1):
        return False
    for char in s1:
           if char in dict.keys():
               dict[char]=dict[char]+1 
           else:
               dict[char]=1
               
    for ch in s2:
        if ch in sec_dict.keys():
            sec_dict[ch]=sec_dict[ch]+1
        else:
            sec_dict[ch]=1
            
    for key in dict.keys():
        if dict[key]>sec_dict.get(key,0):
            return False
    return True 
        

print(randsom("aab","aacb"))
    
           
            
            
            
   
