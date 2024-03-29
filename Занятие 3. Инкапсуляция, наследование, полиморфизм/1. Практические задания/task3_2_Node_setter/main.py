from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        # TODO заменить на вызов setter
        self.next = next_
    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    # TODO заменить на getter и setter
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, value):
        print('Вызван сеттер') # это не нравится кнопке Check
        self.is_valid(value)
        self.__next = value


if __name__ == "__main__":
    first_node = Node(1)  # отработал setter в init
    second_node = Node(2)  # отработал setter в init

    first_node.next = second_node

    print(repr(first_node), repr(first_node.next))
