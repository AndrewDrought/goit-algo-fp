class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

    # Реверсування
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    # Сортування вставками
    def insertion_sort(self):
        sorted_list = LinkedList()
        current_node = self.head
        while current_node:
            sorted_list.insert_sorted(current_node.data)
            current_node = current_node.next
            self.head = sorted_list.head

    def insert_sorted(self, data):
        new_node = Node(data)
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Об’єднання двох відсортованих списків
    def merge_sorted_lists(self, list2):
        merged_list = LinkedList()
        current1 = self.head
        current2 = list2.head
        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.insert(current1.data)
                current1 = current1.next
            else:
                merged_list.insert(current2.data)
                current2 = current2.next
        while current1:
            merged_list.insert(current1.data)
            current1 = current1.next
        while current2:
            merged_list.insert(current2.data)
            current2 = current2.next
        return merged_list


my_list = LinkedList()


for i in range(1, 9):
    my_list.insert(i)

print("Початковий список:")
print(my_list.display())

# Реверсування списку
my_list.reverse()
print("Реверсований список:")
print(my_list.display())

# Сортування списку
my_list.insertion_sort()
print("Відсортований список:")
print(my_list.display())

# Створення другого відсортованого списку
my_second_list = LinkedList()
for i in range(10, 18):
    my_second_list.insert(i)
my_second_list.insertion_sort()

print("Другий відсортований список:")
print(my_second_list.display())

# Об'єднання двох відсортованих списків
merged_list = my_list.merge_sorted_lists(my_second_list)
print("Об'єднаний відсортований список:")
print(merged_list.display())
