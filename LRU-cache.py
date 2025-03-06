"""
Doubly linked list + hashmap approach Practice
# TC - O(1)
# SC - O(1)
"""


class DoublyLL:
    def __init__(self):
        self.key = 0
        self.val = 0

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # hashmap to store key and node reference
        self.cache = {}

        # initialize head and tail for doubly LL
        self.head = DoublyLL()
        self.tail = DoublyLL()

        # create doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

        # size of doublyLL
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        # check if present in hashmap
        # if key not present
        if key not in self.cache: return -1

        # if key present
        node = self.cache[key]

        # move the node to head
        self.move_to_head(node)
        return node.val

    def move_to_head(self, node):
        # remove node from its existing location
        self.remove_node(node)
        # add the removed node to head
        self.add_node(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # add node after head
    def add_node(self, node):
        # create link between new node and the head
        node.next = self.head.next
        node.prev = self.head

        node.next.prev = node
        self.head.next = node

    #    three conditions to keep track of -
    #    1. if newnode already in cache, move the node to the head of the linked list and return value
    #    2. if size < capacity, add new node in cache and add new node to the head of the linked list
    #    3. if size > capacity, remove node from tail, remove the node from cache. add new node to head and cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # get reference
            node = self.cache[key]
            # move node to head
            self.move_to_head(node)
            # update the value to new value
            node.val = value
            return

        if self.capacity == len(self.cache):
            # remove last node
            popped_node = self.pop_tail()
            # remove from cache
            del self.cache[popped_node.key]

        # add new node
        newnode = DoublyLL()
        newnode.key = key
        newnode.val = value
        self.add_node(newnode)
        self.cache[key] = newnode

    def pop_tail(self):
        # pass last node to remove_node method
        res = self.tail.prev
        self.remove_node(res)
        return res

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)