from unittest import TestCase, main
from stack import Node, Stack
from custom_queue import Node, Queue
from linked_list import Node, LinkedList


class TestClasses(TestCase):
    def test_Node(self):
        """
        Тестируем класс Node
        """
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1, n2.next_node)

    def test_Stack(self):
        """
        Тестируем класс Stack и метод push
        """
        stack = Stack()
        stack.push("item1")
        stack.push("item2")
        stack.push("item3")
        self.assertEqual(len(stack.stack_list), 3)
        self.assertEqual(stack.top.data, "item3")
        self.assertEqual(stack.top.next_node.data, "item2")
        self.assertEqual(stack.top.next_node.next_node.data, "item1")
        self.assertEqual(stack.top.next_node.next_node.next_node, None)

    def test_Stack_pop(self):
        """
        Тестируем класс Stack и метод pop
        """
        stack = Stack()
        stack.push("data1")
        data = stack.pop()
        self.assertEqual(stack.top, None)
        self.assertEqual(data, "data1")

        stack = Stack()
        stack.push("data1")
        stack.push("data2")
        data = stack.pop()
        self.assertEqual(stack.top.data, "data1")
        self.assertEqual(data, "data2")

    def test_Queue(self):
        """
        Тестируем класс Queue
        """
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.tail.next_node, None)
        self.assertEqual(queue.dequeue(), "data1")
        self.assertEqual(queue.dequeue(), "data2")
        self.assertEqual(queue.dequeue(), "data3")
        self.assertEqual(queue.dequeue(), None)

    def test_LinkedList(self):
        """
        Тестируем класс LinkedList
        """
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data,  {'id': 0})
        self.assertEqual(ll.tail.data, {'id': 3})


if __name__ == "__main__":
    main()
