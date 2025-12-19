class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return
        
        sorted_head = None
        current = self.head
        
        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node
        
        self.head = sorted_head

    def _sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node
        
        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        return sorted_head

    def merge_with_sorted_list(self, other_list):
        self.head = self._merge_two_lists(self.head, other_list.head)

    def _merge_two_lists(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self._merge_two_lists(left.next, right)
        else:
            result = right
            result.next = self._merge_two_lists(left, right.next)
        
        return result

def main():
    llist1 = LinkedList()
    llist1.insert_at_end(5)
    llist1.insert_at_end(3)
    llist1.insert_at_end(8)
    llist1.insert_at_end(1)
    llist1.insert_at_end(9)
    
    print("list 1")
    llist1.print_list()
    
    print("\nReversed list 1")
    llist1.reverse()
    llist1.print_list()
    
    print("\nSorted list 1")
    llist1.insertion_sort()
    llist1.print_list()
    
    llist2 = LinkedList()
    llist2.insert_at_end(7)
    llist2.insert_at_end(2)
    llist2.insert_at_end(4)
    llist2.insert_at_end(6)
    
    print("\nlist 2")
    llist2.print_list()
    
    print("\nsorted list 2")
    llist2.insertion_sort()
    llist2.print_list()
    
    print("\nmerged")
    llist1.merge_with_sorted_list(llist2)
    llist1.print_list()


if __name__ == "__main__":
    main()