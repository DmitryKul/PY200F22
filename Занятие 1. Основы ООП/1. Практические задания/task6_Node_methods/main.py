from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value# TODO добавить атрибуты
        self.next = next_

    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        return self.value # TODO вернуть значение узла
    def get_next(self) -> Optional['Node']:
        return self.next
    def __repr__(self):
        return('Node')
        # TODO добавить метод next

if __name__ == '__main__':
    second_node = Node(2) # второй узел
    first_node = Node(1, second_node)  # первый узел
    print(first_node.get_next())

    print(first_node.get_next()) # TODO с помощью метода распечатать значение первого узла
    print(second_node.get_next()) # TODO  с помощью метода распечатать следующий узел второго узла
