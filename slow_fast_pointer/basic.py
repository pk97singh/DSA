slow=head 
fast=head 

while(fast!=null and fast.next!=null):
  slow=slow.next() 
 fast=fast.next().next()

return slow
