s1="abcad"
def first_unique_char(s1):
    dict={}
    count=1
    for char in s1:
        if char  in dict.keys():
            dict[char]=dict[char]+1
        else :   
             dict[char]=1
             
    for char in s1:
        if dict[char]==1:
            return char
         

print(first_unique_char(s1))
