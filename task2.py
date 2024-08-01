from LinkedList import LinkedList

# Класс реализующий кольцевой FIFO буфер заданного размера
# Реализация на массиве
class FIFOListWay:
    def __init__(self, max_size: int):
        self.maxsize = max_size
        self.buffer = [None] * self.maxsize
        self.read_index = 0
        self.write_index = 0

    # принимает объект data, добавляет его в буффер
    def push(self, value):
        self.write_index %= self.maxsize
        self.buffer[self.write_index] = value
        self.write_index += 1

    # возвращает и удаляет элемент из буффера по принципу FIFO
    def pop(self):
        self.read_index %= self.maxsize
        res = self.buffer[self.read_index]
        self.buffer[self.read_index] = None
        self.read_index += 1
        return res

    # Возвращает Истина если буфер пустой иначе Ложь
    def is_empty(self):
        i = 0
        while i != self.maxsize:
            if self.buffer[i] is not None:
                return False
            i += 1
        return True

    # Возвращает Истина если буфер полный иначе Ложь
    def is_full(self):
        i = 0
        while i != self.maxsize:
            if self.buffer[i] is None:
                return False
            i += 1
        return True




# Класс реализующий кольцевой FIFO буфер заданного размера
# Реализация на односвязном списке
class FIFOLinkedListWay:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.buffer = LinkedList()
        self.max_size = max_size
        for _ in range(max_size):
            self.buffer.expand(None)
        self.first = self.buffer.head

    # принимает объект data, добавляет его в буффер
    def push(self, data):
        self.buffer.push(data)

    # возвращает и удаляет элемент из буффера по принципу FIFO
    def pop(self):
        res = self.first.data
        self.first.data = None
        self.first = self.first.next
        return res

    # Возвращает Истина если буфер пустой иначе Ложь
    def is_empty(self):
        current = self.first
        for _ in range(self.max_size):
            if current.data is not None:
                return False
            current = current.next
        return True

    # Возвращает Истина если буфер полон иначе Лжь
    def is_full(self):
        current = self.first
        for _ in range(self.max_size):
            if current.data is None:
                return False
            current = current.next
        return True
