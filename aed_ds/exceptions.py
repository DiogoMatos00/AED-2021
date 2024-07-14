class EmptyListException(Exception):
    """Executing non empty list methods on an empty list."""
    def __init__(self, msg):
        self.msg = msg


class InvalidPositionException(Exception):
    """Accessing positions smaller or greater then the number of elements."""
    def __init__(self, msg):
        self.msg = msg


class NoSuchElementException(Exception):
    """Reference to an element not present in the list."""
    def __init__(self, msg):
        self.msg = msg


class EmptyStackException(Exception):
    """Accessing the next element from an empty stack."""
    def __init__(self, msg):
        self.msg = msg


class FullStackException(Exception):
    """Trying to add elements to a full stack."""
    def __init__(self, msg):
        self.msg = msg


class EmptyQueueException(Exception):
    """Accessing the next element from an empty queue."""
    def __init__(self, msg):
        self.msg = msg


class FullQueueException(Exception):
    """Truing to add elements to a fill queue."""
    def __init__(self, msg):
        self.msg = msg


class DuplicatedKeyException(Exception):
    """Trying to insert a pre-existing key."""
    def __init__(self, msg):
        self.msg = msg


class EmptyDictionaryException(Exception):
    """Accessing content from an empty dictionary."""
    def __init__(self, msg):
        self.msg = msg

class EmptyTreeException(Exception):
    """Accessing content from an empty tree."""
    def __init__(self, msg):
        self.msg = msg