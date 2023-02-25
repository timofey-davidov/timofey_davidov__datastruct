class Node:
    """
    Класс для работы с элементами стека: содержит в себе информацию и ссылку на следующий объект стека
    """

    def __init__(self, data, next_node=None):
        if all([next_node is not None,
                not isinstance(next_node, Node)]):
            print("Ошибка следующего узла")
        else:
            self.data = data
            self.next_node = next_node


class Queue:
    """
    Класс для работы с структурой данных ОЧЕРЕДЬ
    """

    def __init__(self, head=None, tail=None):

        # список элементов в очереди
        self.queue_list = list()

        # объекты очереди: начало (head) и конец (tail)
        self.head = head
        self.tail = tail

    def enqueue(self, item):
        """
        Функция, которая добавляет элемент в ОЧЕРЕДЬ
        """
        if len(self.queue_list) == 0:
            self.queue_list.append(Node(item, None))
            self.head = self.tail = self.queue_list[-1]
        else:
            self.queue_list.insert(0, Node(item, None))
            self.queue_list[1].next_node = self.queue_list[0]
            self.tail = self.queue_list[0]
