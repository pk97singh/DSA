def check_validity(src:dict,trg:dict):
    for ch in trg:
        if src.get(ch,0) < trg[ch]:
            return False 
    return True
   


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        high=0
        low=0
        freq={}
        hmap={}
        ans=""
        res=float('inf')
        
        if len(s)==len(t):
            return ""
        
            
            
        for i in range(len(t)):
            hmap[t[i]]=hmap.get(t[i],0)+1
            
        for high in range(len(s)):
            freq[s[high]]=freq.get(s[high],0)+1   
        
            while (check_validity(freq,hmap)):
                 length=high-low+1 
            
                 if length<res:
                    res=length
                    ans=s[low:high+1]
               
                 freq[s[low]]-=1
                 low=low+1
                
        return ans
