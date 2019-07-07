# -*- coding: utf-8 -*-


## 节点类
class Node(object):

    def __init__(self, value, next, *args, **kwargs):
        self.value = value
        self.next = next



## 单链表类
class SinglyLinkedList(object):

    def __init__(self, node_list, *args, **kwargs):
        ## 加入哨兵节点
        self.head = Node(None, None)


    def reverse1(self):

        ## 使用哨兵节点处理掉没有节点的情况
        if not self.head.next:
            return

        temp_node = self.head.next
        while temp_node and temp_node.next:
            """
            每次循环建立后一个节点指向前面节点的指针，然后将后一个节点的value和其下一个节点作为循环起始条件，依次进行
            """
            next_node = temp_node.next
            next_step = next_node.next
            next_node.next = temp_node
            temp_node.next = next_step
            temp_node = next_node

        self.head.next = temp_node


    def reverse2(self):
        """
        单链表反转
        """
        reversed_head = None
        current = self.head
        while current:
            reversed_head, reversed_head._next, current = current, reversed_head, current._next
        return reversed_head


    def find_cycle(self):
        """
        检测链表中的环
        """
        if not self.head.next:
            return False

        start_node = temp_node = self.head.text
        while temp_node and temp_node != self.head:
            if temp_node.next == temp_node:
                return True
            temp_node = temp_node.next

        return False


    # Detect cycle in a list
    # 检测环
    # recommend
    def has_cycle(head: Node) -> bool:
        slow, fast = head, head
        while fast and fast._next:
            slow = slow._next
            fast = fast._next._next
            if slow == fast:
                return True
        return False


    def merge_sorted_linkedlist(self, head1, head2):
        """
        合并有序链表
        """
        if not head1.next or not head2.next:
            return head1.next or head2.next


        head = Node(None, None)
        head1 = linked_list1.head
        head2 = linked_list2.head
        while head1.next and head2.next:

            if head1.next <= head2.next:
                head.next = head1.next
                head1 = head1.next
            else:
                head.next = head2.next
                head2 = head2.next

            head = head.next

        head.next = head1.next if head1.next else head2.next
        return head


    def remove_node_from_end(self, head, n):
        """
        移除链表中倒数第n个结点
        """
        if not head.next or n <= 0:
            return head

        length = 0
        current = head.next
        while current:
            length += 1
            current = current.next

        if n > length:
            return head

        if length == 1:
            head.next = None
            return head

        if n == length:
            head.next = head.next.next
            return head


        loop = 0
        slow, fast = head.next, head.next.next
        while slow and fast:
            loop += 1
            if length - loop == n:
                slow.next = fast.next
                break
            slow, fast = slow.next, fast.next
        return head


    # Remove nth node from the end
    # 删除倒数第n个节点。假设n大于0
    # todo 不判断n？
    def remove_nth_from_end(head: Node, n: int) -> Optional[Node]:
        fast = head
        count = 0
        while fast and count < n:
            fast = fast._next
            count += 1
        if not fast and count < n:  # not that many nodes
            return head
        if not fast and count == n:
            return head._next
        
        slow = head
        while fast._next:
            fast, slow = fast._next, slow._next
        slow._next = slow._next._next
        return head


    def find_middle_node(head):
        """
        找到链表中间结点
        """
        if not head.next:
            return

        if not head.next.next:
            return head.next

        slow, fast = head
        while slow and fast:
            slow, fast = slow.next, fast.next
            if not fast:
                return slow
            elif not fast.next:
                return slow, slow.next


    def find_middle_node(head: Node) -> Optional[Node]:
        """
        找到链表中间结点
        todo: 不区分上中结点还是下中结点？
        """
        slow, fast = head, head
        fast = fast._next if fast else None
        while fast and fast._next:
            slow, fast = slow._next, fast._next._next
        return slow



















