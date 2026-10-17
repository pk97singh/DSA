# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
#madam=madam ,radar,civic if we read backward still word will be same


def longest_palindrome(s1):
    dict={}
    count=0
    for char in s1:
        dict[char]=dict.get(char,0)+1
        
    for c in dict.values():
        if c%2==0:
            count=count+c
        else:
            count=count+(c-1)
    if count<len(s1):
        count=count+1
    return count

print(longest_palindrome("abccccdd"))
