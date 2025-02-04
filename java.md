
Remove every k-th node of the linked list
Last Updated : 16 Sep, 2024
Given a singly linked list, the task is to remove every kth node of the linked list. Assume that k is always less than or equal to the length of the Linked List.

Examples :

Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6, k = 2
Output: 1 -> 3 -> 5
Explanation: After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 .


Input: LinkedList: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10, k = 3
Output: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
Explanation: After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.



// Java program to delete every k-th Node of
// a singly linked list.
class Node {
int data;
Node next;

    Node(int newData) {
        data = newData;
        next = null;
    }
}

public class GfG {

    // Function to remove every kth node in the
    // linked list
    static Node deleteK(Node head, int k) {
      
        // If list is empty or k is 0, return the head
        if (head == null || k <= 0)
            return head;

        Node curr = head;
   
        Node prev = null;
      
        int count = 0;

        // Traverse the linked list
        while (curr != null) {
          
            // Increment the counter for each node
            count++;

            // If count is a multiple of k, remove 
            // current node
            if (count % k == 0) {
              
                // skip the current node
                if (prev != null) {
                    prev.next = curr.next;
                } 
               else {
                 
                    // If removing the head node
                    head = curr.next;
                }
            } 
           else {
             
                // Update previous node pointer only if
                // we do not remove the node
                prev = curr;
            }
            curr = curr.next;
        }

        return head;
    }

    static void printList(Node head) {
 
        Node curr = head;
        while (curr != null) {
            System.out.print(curr.data + " ");
            curr = curr.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
      
        // Create a hard-coded linked list: 
        // 1 -> 2 -> 3 -> 4 -> 5 -> 6
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        head.next.next.next.next.next = new Node(6);
        int k = 2;

        head = deleteK(head, k);

        printList(head);
    }
}


/*
Given a singly linked list, the task is to find the middle of the linked list. If the number of nodes are even, then there would be two middle nodes, so return the second middle node.

Example:

Input: linked list: 1->2->3->4->5
Output: 3
Explanation: There are 5 nodes in the linked list and there is one middle node whose value is 3.


Input: linked list = 10 -> 20 -> 30 -> 40 -> 50 -> 60
Output: 40
Explanation: There are 6 nodes in the linked list, so we have two middle nodes: 30 and 40, but we will return the second middle node which is 40.


Middle-of-a-Linked-List4
*/

// Java program to illustrate how to find the middle element
// by counting the number of nodes

// A singly linked list node
class Node {
int data;
Node next;

    // Constructor to initialize a new node with data
    Node(int x) {
        this.data = x;
        this.next = null;
    }
}

class GfG {

    // Helper function to find length of linked list
    static int getLength(Node head) {

        // Variable to store length
        int length = 0;

        // Traverse the entire linked list and increment
        // length by 1 for each node
        while (head != null) {
            length++;
            head = head.next;
        }

        // Return the number of nodes in the linked list
        return length;
    }

    // Function to get the middle value of the linked list
    static int getMiddle(Node head) {
      
        // Finding the length of the list
        int length = getLength(head);

        // traverse till we reached half of length
        int mid_index = length / 2;
        while (mid_index > 0) {
            head = head.next;
            mid_index--;
        }
        // temp will be storing middle element
        return head.data;
    }

    public static void main(String[] args) {

        // Create a hard-coded linked list:
        // 10 -> 20 -> 30 -> 40 -> 50 -> 60 
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        head.next.next.next = new Node(40);
        head.next.next.next.next = new Node(50);
        head.next.next.next.next.next = new Node(60);

        System.out.println(getMiddle(head));
    }
}

/*Count Occurrences in a Linked List
Last Updated : 28 Oct, 2024
Given a singly linked list and a key, the task is to count the number of occurrences of the given key in the linked list.

Example :

Input : head: 1->2->1->2->1->3->1 , key = 1
Output : 4


Count-Occurrences-in-a-Linked-List_1
Explanation: key equals 1 has 4 occurrences.


Input : head: 1->2->1->2->1, key = 3
Output : 0
Explanation: key equals to 3 has 0 occurrences.

*/

// Java program to count occurrences in
// a linked list by recursion
class Node {
int data;
Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class GfG {

    // Recursive method to count occurrences of a
      // value in the linked list
    static int count(Node head, int key) {
        if (head == null) {
            return 0;
        }
          
          int ans = count(head.next, key);
      
        if (head.data == key) {
            ans++;
        }
        
          return ans;
    }

    public static void main(String[] args) {
      
        // Hard coded linked list: 
          // 1 -> 2 -> 1 -> 2 -> 1
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(1);
        head.next.next.next = new Node(2);
        head.next.next.next.next = new Node(1);

        int key = 1;

        System.out.println(count(head, key));
    }
}


/*Traversal of Circular Linked List
Last Updated : 12 Sep, 2024
Given a circular linked list, the task is to print all the elements of this circular linked list.

*/

// Java program to traverse a circular
// linked list.

class Node {
int data;
Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class GfG {

    static void printList(Node curr, Node head) {

        // return if list is empty
        if (head == null) return;
        
        System.out.print(curr.data + " ");
        
        if (curr.next == head)
            return;
        
        printList(curr.next, head);

    }

    public static void main(String[] args) {
          
          // Create a hard-coded linked list
        // 11 -> 2 -> 56 -> 12
        Node head = new Node(11);
        head.next = new Node(2);
        head.next.next = new Node(56);
        head.next.next.next = new Node(12);

        head.next.next.next.next = head;

        printList(head, head);
    }
}

/*Check if a linked list is Circular Linked List
Last Updated : 26 Aug, 2024
Given the head of a singly linked list, the task is to find if given linked list is circular or not. A linked list is called circular if its last node points back to its first node.

Note: The linked list does not contain any internal loops.

Example:
Input: LinkedList: 2->4->6->7->5

Output: true
Explanation: As shown in figure the first and last node is connected, i.e. 5 -> 2

Input: LinkedList: 2->4->6->7->5->1

Output: false
Explanation: As shown in figure this is not a circular linked list.*/

// Java program to check if
// linked list is circular

class Node {
int data;
Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class GfG {

    // Function to check if the linked list is circular
    static boolean isCircular(Node head) {
        // If head is null, list is empty, circular
        if (head == null) return true;

        Node temp = head;

        // Traverse until the end is reached or
        // the next node equals the head
        while (head != null && head.next != temp)
            head = head.next;

        // If end reached before finding head again,
        // list is not circular
        if (head == null || head.next == null)
            return false;

        // If head found again, list is circular
        return true;
    }

    public static void main(String[] args) {
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);

        // Check if the linked list is circular
        System.out.println(isCircular(head) ? "Yes" : "No");

        // Making the linked list circular
        head.next.next.next.next = head;

        // Check again if the linked list is circular
        System.out.println(isCircular(head) ? "Yes" : "No");
    }
}


/*
Count nodes in Circular linked list
Last Updated : 31 Aug, 2024
Given a circular linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

*/

// Java program to count number of nodes
// in a circular linked list

class Node {
int data;
Node next;

    Node(int new_data) {
        data = new_data;
        next = null;
    }
}

// Function to count nodes in a given Circular
// linked list
class GfG {

    static int countNodes(Node head) {
        if (head == null) return 0;

        Node curr = head;
        int result = 0;

        do {
            curr = curr.next;
            result++;
        } while (curr != head);

        return result;
    }

    public static void main(String[] args) {
        
        // Create list: 1->2->3->4->5--->1
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        head.next.next.next.next.next = head;

        System.out.println(countNodes(head));
    }
}

/*
Deletion from a Circular Linked List
Last Updated : 19 Dec, 2024
In this article, we will learn how to delete a node from a circular linked list. In a circular linked list, the last node connects back to the first node, creating a loop.

There are three main ways to delete a node from circular linked list:

Deletion at the beginning
Deletion at specific position
Deletion at the end
Now, let’s look at the methods and steps for these three deletion operations.

Deletion from a Circular Linked List:
Deletion involves removing a node from the linked list. The main difference is that we need to ensure the list remains circular after the deletion. We can delete a node in a circular linked list in three ways:

1. Deletion from the beginning of the circular linked list
   To delete the first node of a circular linked list, we first check if the list is empty. If it is then we print a message and return NULL. If the list contains only one node (the head is the same as the last) then we delete that node and set the last pointer to NULL. If there are multiple nodes then we update the last->next pointer to skip the head node and effectively removing it from the list. We then delete the head node to free the allocated memory. Finally, we return the updated last pointer, which still points to the last node in the list.


*/

class Node {
int data;
Node next;

    Node(int value) {
        data = value;
        next = null;
    }
}

public class GFG {
public static Node deleteFirstNode(Node last) {
if (last == null) {
// If the list is empty
System.out.println("List is empty");
return null;
}

        Node head = last.next;

        if (head == last) {
            // If there is only one node in the list
            last = null;
        } else {
            // More than one node in the list
            last.next = head.next;
        }

        return last;
    }

    public static void printList(Node last) {
        if (last == null) return;

        Node head = last.next;
        while (true) {
            System.out.print(head.data + " ");
            head = head.next;
            if (head == last.next) break;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Create circular linked list: 2, 3, 4
        Node first = new Node(2);
        first.next = new Node(3);
        first.next.next = new Node(4);

        Node last = first.next.next;
        last.next = first;

        System.out.print("Original list: ");
        printList(last);

        // Delete the first node
        last = deleteFirstNode(last);

        System.out.print("List after deleting first node: ");
        printList(last);
    }
}
/*Output
Original list: 2 3 4
List after deleting first node: 3 4
*/

class Node {
int data;
Node next;
Node(int value){
data = value;
next = null;
}
}

public class GFG {
public static Node deleteSpecificNode(Node last,
int key){
if (last == null) {
// If the list is empty
System.out.println(
"List is empty, nothing to delete.");
return null;
}
Node curr = last.next;
Node prev = last;

        // If the node to be deleted is the only node in the
        // list
        if (curr == last && curr.data == key) {
            last = null;
            return last;
        }

        // If the node to be deleted is the first node
        if (curr.data == key) {
            last.next = curr.next;
            return last;
        }

        // Traverse the list to find the node to be deleted
        while (curr != last && curr.data != key) {
            prev = curr;
            curr = curr.next;
        }

        // If the node to be deleted is found
        if (curr.data == key) {
            prev.next = curr.next;
            if (curr == last) {
                last = prev;
            }
        }
        else {
            // If the node to be deleted is not found
            System.out.println("Node with data " + key
                               + " not found.");
        }
        return last;
    }

    public static void printList(Node last){
        if (last == null) {
            System.out.println("List is Empty");
            return;
        }
      
        Node head = last.next;
        while (true) {
            System.out.print(head.data + " ");
            head = head.next;
            if (head == last.next)
                break;
        }
        System.out.println();
    }

    public static void main(String[] args){
        // Create circular linked list: 2, 3, 4
        Node first = new Node(2);
        first.next = new Node(3);
        first.next.next = new Node(4);

        Node last = first.next.next;
        last.next = first;

        System.out.print("Original list: ");
        printList(last);

        // Delete a specific node
        int key = 3;
        last = deleteSpecificNode(last, key);

        System.out.print("List after deleting node " + key
                         + ": ");
        printList(last);
    }
}

/*Original list: 2 3 4
List after deleting node 3: 2 4
*/