"""
File: add2.py
Name: Jennifer Li
------------------------
This program adds two numbers which are stored as
the type of linked-list. Notice that the numbers
are stored reversely, and the length of two linked-list
might be different. After the plus of two numbers, the
result also has to be stored as linked-list reversely.

If you execute this program in terminal, you will the
result like below,
----------test1----------
l1: 2->4->3
l2: 5->6->4
ans: 7->0->8
----------test2----------
l1: 9->9->9->9->9->9->9
l2: 9->9->9->9
ans: 8->9->9->9->0->0->0->1
----------test3----------
l1: 0
l2: 0
ans: 0
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    This function adds two numbers, which are stored as linked-list reversely,
    and also stores the result of plus reversely as linked-list. There are
    several procedures will be followed in this function.

    1) loop over the linked-list, l1 and l2, to store the two number into two str.
    2) change the data type from str to int, do the plus, and change the data
       type back to str.
    3) loop over the result str reversely to convert it to a new data structure,
       linked-list, and then return it.

    :param l1: ListNode, the head of a linked-list, storing the first number reversely
    :param l2: ListNode, the head of a linked-list, storing the second number reversely
    :return linked_list: ListNode, the head of a linked-list, storing the result reversely
    """
    cur1 = l1
    cur2 = l2
    str1 = ''
    str2 = ''
    while cur1 or cur2:  # the length of cur1 and cur2 might be different
        if cur1:
            str1 = str(cur1.val) + str1  # convert reverse to forward
            cur1 = cur1.next
        if cur2:
            str2 = str(cur2.val) + str2  # convert reverse to forward
            cur2 = cur2.next
    num1 = int(str1)
    num2 = int(str2)
    ans = str(num1 + num2)
    linked_list = None
    for i in range(len(ans) - 1, -1, -1):  # loop over the ans reversely
        node = ListNode(int(ans[i]), None)
        if linked_list is None:  # first node
            linked_list = node
            cur = linked_list  # make cur stand on the last node
        else:
            cur.next = node
            cur = cur.next
    return linked_list


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
