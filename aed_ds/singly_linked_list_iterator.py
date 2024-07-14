from aed_ds.exceptions import NoSuchElementException
from aed_ds.adt_iterator import Iterator

class SinglyLinkedListIterator(Iterator):
    def __init__(self, head):
        self.head = head
        self.current = None

    def has_next(self) -> bool:
        if self.head == None:
            return False
        elif self.current != None:
            if self.current.next_node == None:
                return False
        
            return True
        
        return True
           
                  
    def get_next(self) -> object:
        
        if self.current == None:
            if self.head == None:
                raise NoSuchElementException("Erro")  
            
            self.current = self.head
            current = self.current.element
            return current
        if self.current.next_node != None:
            self.current = self.current.next_node
            current = self.current.element
            return current
        
        raise NoSuchElementException("Erro")  


    def rewind(self) -> None:
        self.current = None