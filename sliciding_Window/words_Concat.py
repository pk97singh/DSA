
class Solution:
    def findSubstring(self, s, words) :
        
        word_len=len(words[0])
        word_Count = len(words) 
        
        
        need={}
        freq={}
        count=0
        ans=[]
        for word in words:
            need[word]=need.get(word,0)+1
            
        for offset in range(word_len):
            left=offset
            
            for right in range(offset,len(s)-word_len+1,word_len):
                word=s[right:right+word_len]
               
                if word not in need:
                    freq={}
                    count=0
                    left=right+word_len
                    continue
                
                freq[word]=freq.get(word,0)+1
                count +=1
                
                while freq[word]>need[word]:
                    left_word=s[left:left+word_len]
                    freq[left_word]-=1
                    left+=word_len 
                    count-=1
                    
                if count == word_Count:
                    ans.append(left)
                   
                                       # Move forward to search for another window
                    left_word = s[left:left + word_len]
                    freq[left_word] -= 1
                    left += word_len
                    count -= 1
            return ans
                






print(Solution().findSubstring("barfoothefoobarman",["foo","bar"]))

