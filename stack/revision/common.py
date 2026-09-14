#check valid brackets
s1="{[()]}"
stack=[]
for ch in s1:
    if ch in "{([":
        stack.append(ch)
        continue
    if not stack:
        print("false")
        break
            
    top=stack[-1]
    if ((ch =="}" and top !="{" ) or 
       (ch ==")" and top !="(" ) or 
       (ch =="]" and top !="[" )):
           print("false")
           break
           
    stack.pop()
    
if len(stack)==0:
        print("true")
