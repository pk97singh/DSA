def check_validity(src:dict,tgt:dict):
    for ch in tgt:
        if src.get(ch,0)<tgt[ch]:
            return False 
    return True

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        h=0
        l=0
        hmap={}
        freq={}
        res=float('inf')

        for word in words:
            for ch in range(len(word)):
                hmap[word[ch]]=hmap.get(word[ch],0)+1

        for h in range(len(s)):
            freq[s[h]]=freq.get(s[h],0)+1

            while(check_validity(freq,hmap)):
                length=h-l+1


                if length<res:
                    res=length 
                    ans=[l,h]

                freq[s[l]]-=1
                l=l+1


        return ans
            

           
        
