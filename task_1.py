class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")

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
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            
            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current

            current = next_node

        self.head = sorted_head

def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    dummy = Node()
    tail = dummy

    head1 = list1.head
    head2 = list2.head

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

if __name__ == "__main__":
    print("--- 1. Тест реверсування ---")
    ll1 = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll1.append(val)
    print("Оригінальний список:")
    ll1.print_list()
    ll1.reverse()
    print("Реверсований список:")
    ll1.print_list()

    print("\n--- 2. Тест сортування вставками ---")
    ll2 = LinkedList()
    for val in [4, 1, 3, 2, 5]:
        ll2.append(val)
    print("Невідсортований список:")
    ll2.print_list()
    ll2.insertion_sort()
    print("Відсортований список:")
    ll2.print_list()

    print("\n--- 3. Тест об'єднання двох відсортованих списків ---")
    list_a = LinkedList()
    for val in [1, 3, 5, 7]:
        list_a.append(val)

    list_b = LinkedList()
    for val in [2, 4, 6, 8]:
        list_b.append(val)

    print("Список A:")
    list_a.print_list()
    print("Список B:")
    list_b.print_list()

    merged = merge_sorted_lists(list_a, list_b)
    print("Об'єднаний відсортований список:")
    merged.print_list()