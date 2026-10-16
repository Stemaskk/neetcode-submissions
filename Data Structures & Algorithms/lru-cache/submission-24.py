class Node: # Each node will be a cache block
    def __init__(self, key: int, value: int, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    """
    What is a cache

    "Temporary" memory that acts as a bridge between RAM and memory

    LRU keeps track of what was used longest time ago

    So we should have a deque to store the Key ins and outs

    It runs in O(1) average compared to other types like list, which would take O(n) if popped the front

    First In First Out -> FIFO

    If the existing key was used and it is in the middle of a deque it won't be O(1) anymore

    Also checking if a key is in a deque won't be O(1) anyways

    I am leaning towards another hashtable, that would also store keys but for its values it has the LRU


    Just realized that we have capacity to initialize a Cache

    Meaning we can probably make a fixed size array and use it like a cache, and we will store a list to store key, value, and priority

    Nah I got spoiled, we will have a linked list

    Make new node if < capacity

    """

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Dummy start node, we will always use start.next
        self.start = Node(0, 0)
        self.end = self.start

        # Provides direct access to any nodes
        self.seen = dict()

    def move_to_end(self, hold):
        if hold is self.end:
            return
        temp = hold.prev
        temp.next = hold.next
        hold.next.prev = temp
        hold.next = None
        self.end.next = hold
        hold.prev = self.end
        self.end = hold

    def get(self, key: int) -> int:
        if key not in self.seen:
            return -1
        hold = self.seen[key]
        self.move_to_end(hold)
        return hold.value

    def put(self, key: int, value: int) -> None:
        if key in self.seen:
            hold = self.seen[key]
            hold.value = value
            self.move_to_end(hold)
            return

        self.end.next = Node(key, value)
        self.end.next.prev = self.end
        self.end = self.end.next
        self.seen[key] = self.end

        if self.capacity > 0:
            self.capacity -= 1
        else:
            self.start = self.start.next
            del self.seen[self.start.key]