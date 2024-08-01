# Класс реализующий элемент списка
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Класс реализующий односвязный список
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Принимает объект data и добавляет его в список с хвоста
    def push(self, data):
        if not self.head:
            return Exception("Null List")
        else:
            self.tail.data = data
            self.tail = self.tail.next

    # Принимает объект data и добавляет его в список, расширяя его на 1 элемент
    def expand(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    # Возвращает значение головы и удаляет его из списка
    def pop(self):
        res = self.head.data
        self.head.data = None
        self.head = self.head.next
        return res