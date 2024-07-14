from .nodes import SingleListNode
from aed_ds.exceptions import EmptyListException, InvalidPositionException
from .singly_linked_list_iterator import SinglyLinkedListIterator
from aed_ds.adt_list import List

class SinglyLinkedList(List):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        if self.head == None:
            return True

    def size(self):
        return self.count

    def get_first(self):
        if self.head == None:
            raise EmptyListException("Erro")
        return self.head.element

    def get_last(self):
        if self.head == None:
            raise EmptyListException("Erro")
        return self.tail.element

    def get(self, position):
        if position == 0:
            return self.get_first()
        elif position == self.size()-1:
            return self.get_last()
        elif position < 0 or position >= self.size():
            raise InvalidPositionException("Erro")
        else:
            last = self.head
            for _ in range(position):
                last = last.next_node
            return last.element

    def find(self, element):
        count = 0
        last = self.head
        while last:
            if last.element == element:
                return count
            count += 1
            last = last.next_node
        return -1

    def insert_first(self, element):
        element = SingleListNode(element, None)
        if self.head == None:
            self.head = element
            self.tail = element
            self.count += 1
        elif self.tail == None:
            element.set_next_node(self.head)
            self.tail = self.head
            self.head = element
            self.count += 1
        else:
            element.set_next_node(self.head)
            self.head = element
            self.count += 1

    def insert_last(self, element):
        element = SingleListNode(element, None)
        if self.head == None:
            self.head = element
            self.tail = element
            self.count += 1
            return

        last = self.tail
        last.set_next_node(element)
        self.tail = element
        self.count += 1

    def insert(self, element, position):
        if position < 0 or position > self.size():
            raise InvalidPositionException("Erro")
        elif position == 0:
            return self.insert_first(element)
        elif position == self.size():
            return self.insert_last(element)
        else:
            element = SingleListNode(element, None)
            last = self.head
            for _ in range(position-1):
                last = last.next_node
            element.set_next_node(last.next_node)
            last.set_next_node(element)
            self.count += 1

    def remove_first(self):
        if self.head == None:
            raise EmptyListException("Erro")
        save = self.head.element
        self.head = self.head.next_node
        self.count -= 1
        return save

    def remove_last(self):
        if self.head == None:
            raise EmptyListException("Erro")
        if self.size() == 1:
            save = self.head.element
            self.head = None
            self.count -= 1
            return save
        save = self.tail.element
        last = self.head
        for _ in range(self.size()-2):
            last = last.next_node
        last.set_next_node(None)
        self.tail = last
        self.count -= 1
        return save

    def remove(self, position):
        if position < 0 or position >= self.size():
            raise InvalidPositionException("Erro")
        elif self.head == None:
            raise EmptyListException("Erro")
        elif position == 0:
            return self.remove_first()
        elif position == self.size()-1:
            return self.remove_last()
        else:
            last = self.head
            for _ in range(position-1):
                last = last.next_node
            removed_element = last.next_node
            last.set_next_node(removed_element.next_node)
            self.count -= 1
            return removed_element.element


    def make_empty(self) -> None:
        self.head = None
        self.tail = None

    def iterator(self):
        return SinglyLinkedListIterator(self.head)