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


class Stack:
    """
    Класс для создания стека
    """

    def __init__(self):

        # список элементов в стеке
        self.stack_list = list()

        # последний элемент стека
        self.top = None

    def push(self, item):
        """
        Функция для добавления элемента в стек
        :param item: данные
        :return: None
        """
        if len(self.stack_list) == 0:
            self.stack_list.append(Node(item, None))
        else:
            self.stack_list.append(
                Node(item, self.stack_list[-1]))
        self.top = self.stack_list[-1]

    def pop(self):
        """
        Функция для удаления последнего элемента из стека
        """
        if len(self.stack_list) == 0:
            return None
        else:
            last_item = self.stack_list.pop(-1)
            if len(self.stack_list) != 0:
                self.top = self.stack_list[-1]
            else:
                self.top = None
            return last_item.data
