from aed_ds.adt_dictionary import Dictionary
from ctypes import py_object
from aed_ds.singly_linked_list import SinglyLinkedList
from aed_ds.exceptions import NoSuchElementException, DuplicatedKeyException
from aed_ds.item import Item
from aed_ds.adt_list import List


class OpenHashTable(Dictionary):
    def __init__(self, size:int):       
        self.max = size #Tamanho completo do array
        self.inc = 0
        array_type = py_object * self.max #py_object cria um objeto para cada tamanho da lista que serve como posição, o py_object é um espaço
        self.table = array_type() #array_type dá o tipo do array a variável que quisermos
        for i in range (size):    #Criar um array do ctypes e preenche com SinglyLinkedLists criadas por nós
            self.table[i] = SinglyLinkedList()
    
    def hashfunction(self,k):
        return k % self.max
        
    def size(self) -> int:
        return self.inc


    def is_full(self) -> bool:
        return self.inc >= self.max

    def get(self, k: object) -> object:
        n = self.hashfunction(k)
        m = self.table[n].iterator()
        for i in range(self.table[n].size()):
            item = m.get_next()
            if k == item.get_key():
                return item.get_value()
       
        raise NoSuchElementException ("Erro")

        """Returns the value associated with key k.

        Throws NoSuchElementException"""

    def insert(self, k: object, v: object) -> None:
        n = self.hashfunction(k)
        m = self.table[n].iterator()
        for i in range(self.table[n].size()):
            v =  m.get_next()
            if k == v.get_key():
                raise DuplicatedKeyException ("Erro")
        item = Item(k,v)  #item da classe Item (Estamos apenas a instanciar o objeto com recurso a classe Item)
        self.table[n].insert_first(item)
        self.inc += 1

        """Inserts a new value, associated with key k.

        Throws DuplicatedKeyException"""

    def update(self, k: object, v: object) -> None:
        n = self.hashfunction(k)
        m = self.table[n].iterator()  #Retorna o iterador
        for i in range(self.table[n].size()): # percorre o tamanho da lista na posição n
            item = m.get_next()
            if k == item.get_key():
                item.set_value(v)
                return
                    
        raise NoSuchElementException ("Erro")
        """Updates the value associated with key k.

        Throws NoSuchElementException"""

    def remove(self, k: object) -> object:
        n = self.hashfunction(k)
        m = self.table[n].iterator()  #Retorna o iterador
        count = 0
        for i in range(self.table[n].size()): # percorre o tamanho da lista na posição n
            item = m.get_next() 
            save = item.get_value()
            if k == item.get_key():
                self.table[n].remove(count)
                self.inc -= 1
                return save
            count += 1
        raise NoSuchElementException("Erro")


        """Removes the item with key k, and returns the value associated with it.

        Throws NoSuchElementException"""

    def keys(self) -> List:
        l = SinglyLinkedList()
        for i in range(self.max):
            m = self.table[i].iterator()                         # self.table[i] é uma SinglyLinkedList
            for j in range(self.table[i].size()):
                item = m.get_next()
                l.insert_first(item.get_key())
        return l




        """Returns a List with all the keys in the dictionary."""

   
    def values(self) -> List:
        l = SinglyLinkedList()
        for i in range(self.max):
            m = self.table[i].iterator()                         # self.table[i] é uma SinglyLinkedList
            for j in range(self.table[i].size()):
                item = m.get_next()
                l.insert_first(item.get_value())
        return l
        """Returns a List with all the values in the dictionary."""


    def items(self) -> List:
        l = SinglyLinkedList()
        for i in range(self.max):
            m = self.table[i].iterator()                         # self.table[i] é uma SinglyLinkedList
            for j in range(self.table[i].size()):
                item = m.get_next()
                l.insert_first(item)
        return l
        """Returns a List with all the key value pairs in the dictionary."""
