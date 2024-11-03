class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Функція для додавання нового вузла в кінець списку
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Функція для реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Функція для виводу елементів списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

    # Додавання сортування у клас LinkedList
    def merge_sort(self):
        self.head = merge_sort(self.head)

    # Додавання функції об'єднання двох відсортованих списків
    def merge_with(self, other):
        self.head = merge_two_sorted_lists(self.head, other.head)


# Функція для сортування однозв'язного списку злиттям
def merge_sort(head):
    if not head or not head.next:
        return head

    # Функція для пошуку середини списку
    def get_middle(node):
        if not node:
            return node
        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Функція для злиття двох відсортованих списків
    def sorted_merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data <= right.data:
            result = left
            result.next = sorted_merge(left.next, right)
        else:
            result = right
            result.next = sorted_merge(left, right.next)
        return result

    # Рекурсивний розподіл на половини та сортування
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left_list = merge_sort(head)
    right_list = merge_sort(next_to_middle)

    return sorted_merge(left_list, right_list)

# Функція для об'єднання двох відсортованих списків
def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next

# Приклад використання
if __name__ == "__main__":
    print("Список 1:")
    list_1 = LinkedList()
    list_1.append(3)
    list_1.append(5)
    list_1.append(4)
    list_1.append(8)
    list_1.print_list()

    print("Відсортований Список 1:")
    list_1.merge_sort()
    list_1.print_list()

    print("Список 2:")
    list_2 = LinkedList()
    list_2.append(1)
    list_2.append(9)
    list_2.append(2)
    list_2.print_list()

    # Відсортуємо список 2 перед об'єднанням
    print("Відсортований Список 2:")
    list_2.merge_sort()
    list_2.print_list()

    print("Об'єднання Списків 1 та 2:")
    list_1.merge_with(list_2)
    list_1.print_list()

    print("Реверсований об'єднаний список:")
    list_1.reverse()
    list_1.print_list()

