class Node:
    """
    Класс для работы с элементами связного списка: содержит в себе информацию и ссылку на следующий объект вязного списка
    """

    def __init__(self, data, next_node=None):
        if all([next_node is not None,
                not isinstance(next_node, Node)]):
            print("Ошибка следующего узла")
        else:
            self.data = data
            self.next_node = next_node

class LinkedList:
    """
    Класс для работы со связанным списком
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        """
        Функция для добавления элемента в начало списка
        """
        item = Node(data)
        if self.head is not None:
            item.next_node = self.head
        self.head = item
        if self.tail is None:
            self.tail = self.head

    def to_list(self):
        item_lst = list()
        current_node = self.head
        while current_node:
            item_lst.append(current_node.data)
            current_node = current_node.next_node
        return item_lst

    def get_data_by_id(self, id):
        for i in self.to_list():
            try:
                if i["id"] == id:
                    return i
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")

    def insert_at_end(self, data):
        """
        Функция для добавления элемента в конец списка
        """
        item = Node(data)
        if self.tail is not None:
            self.tail.next_node = item
        self.tail = item
        if self.head is None:
            self.head = self.tail

    def print_ll(self):
        """
        Метод вывода односвязного списка
        """
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)
        return ll_string

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end('idusername')
    ll.insert_at_end([1, 2, 3])
    ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
    print(ll.to_list())
    user_data = ll.get_data_by_id(2)
    print(user_data)