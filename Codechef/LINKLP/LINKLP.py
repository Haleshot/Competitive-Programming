def solve(head):
    #Return -1 if no loop exists else return the size of the loop
    s=head
    f=s
    c=0
    if(s!=None):
        while(s!=None and f!=None and s.next!=None and f.next!=None):
            s=s.next     
            f=f.next.next           
            if(f==s):
                c+=1
                break
    s=s.next
    c1=1
    if(c!=0):
        while(s.next!=None):
            s=s.next
            c1+=1
            if(s==f):break
        return c1
    if(c==0):
        return -1