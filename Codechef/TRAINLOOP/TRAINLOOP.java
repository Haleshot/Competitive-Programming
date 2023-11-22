/* Linked List Node
struct Node {
    int data;
    struct Node next;
    Node(int x) {
        data = x;
        next = null;
    }
}; */
class Solution
{
    Node removeDuplicates(Node head) 
    {
         // Your code here
        HashSet<Integer> hs = new HashSet<>(); 
        Node curr=head;
        Node prev=null;
         
        while(curr!=null){
            int val = curr.data;
            if (hs.contains(val))
                prev.next=curr.next;
                    
            else{
                hs.add(val);
                prev=curr;
            }
                 
            curr=curr.next;
        }
       
        return head;
    }
}