"""
File: palindrome_check.py
Name: Jennifer Li
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def palindrome_check(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    cur = head
    head_old = ListNode(cur.val)
    cur_old = head_old
    while cur.next:
        cur = cur.next
        head_old.next = ListNode(cur.val)
        head_old = head_old.next

    cur = head
    back = None
    while cur:
        temp = cur.next
        cur.next = back
        back = cur
        cur = temp

    cur_back = back
    while cur_old:
        if cur_old.val != cur_back.val:
            return False
        cur_old = cur_old.next
        cur_back = cur_back.next
    return True

    # check = []
    # cur = head
    # while cur:
    #     check.append(cur.val)
    #     cur = cur.next
    #
    # check_1 = []
    # for i in range(len(check)):
    #     check_1.append(check[len(check)-1-i])
    #
    # # if check == check_1:
    # #     return True
    # # return False
    #
    # cur_1 = ListNode(0)
    # cur_1_1 = cur_1
    # for val in check_1:
    #     cur_1.next = ListNode(val)
    #     cur_1 = cur_1.next
    #
    # cur = head
    # cur_1 = cur_1_1.next
    # while cur_1:
    #     if cur.val != cur_1.val:
    #         return False
    #     cur = cur.next
    #     cur_1 = cur_1.next
    #
    # return True

####### DO NOT EDIT CODE BELOW THIS LINE ########


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 palindrome_check.py test1"')
    else:
        if args[0] == 'test1':
            ans1 = palindrome_check(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
            if ans1:
                print('1->2->2->1 is palindrome linked lists.')
            else:
                print('1->2->2->1 is not palindrome linked lists.')
            ans2 = palindrome_check(ListNode(1, ListNode(2)))
            if ans2:
                print('1->2 is palindrome linked lists.')
            else:
                print('1->2 is not palindrome linked lists.')
            ans3 = palindrome_check(ListNode(1, ListNode(4, ListNode(3, ListNode(4, ListNode(3, ListNode(1)))))))
            if ans3:
                print('1->4->3->4->3->1 is palindrome linked lists.')
            else:
                print('1->4->3->4->3->1 is not palindrome linked lists.')
            ans4 = palindrome_check(ListNode(1, ListNode(2, ListNode(1, ListNode(1, ListNode(2, ListNode(1)))))))
            if ans4:
                print('1->2->1->1->2->1 is palindrome linked lists.')
            else:
                print('1->2->1->1->2->1 is not palindrome linked lists.')
            ans5 = palindrome_check(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
            if ans5:
                print('1->2->3->4->5->6 is palindrome linked lists.')
            else:
                print('1->2->3->4->5->6 is not palindrome linked lists.')
            ans6 = palindrome_check(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1))))))
            if ans6:
                print('1->2->3->2->1 is palindrome linked lists.')
            else:
                print('1->2->3->2->1 is not palindrome linked lists.')
        else:
            print('Error: Please type"python3 palindrome_check.py test1"')


if __name__ == '__main__':
    main()
