# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        """
        [   LT] - [MH reversed ] - [  ]
        """

        if left == right:
            return head
        
        currIndex = 1

        dummyNode = ListNode()

        currNode = head
        prevNode = dummyNode
        leftTail = None
        middleHead = None

        temp = None
        
        while currNode:
            if currIndex == left:
                # start reversing
                leftTail = prevNode
                middleHead = currNode
                leftTail.next = None
                prevNode = currNode
                currNode = currNode.next

            elif currIndex == right:
                # end reversing
                leftTail.next = currNode
                middleHead.next = currNode.next

                if left == 1:
                    head = currNode

                temp = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = temp
                
                break
                
            elif left < currIndex < right:
                temp = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = temp

            else:
                prevNode = currNode
                currNode = currNode.next

            currIndex += 1

        return head




