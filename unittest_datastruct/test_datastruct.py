from unittest import TestCase, main
from classes import Node, Stack

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

if __name__ == "__main__":
    main()
