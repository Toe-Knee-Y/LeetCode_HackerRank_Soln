class LRUCache:

    # we have to use a doubly linked list
    def __init__(self, capacity: int):
        self.linkedlist = DoublyLinkedList()
        # I want to decrement the counter for capacity util
        # it reaches 0
        self.capacity = capacity
        self.hashtable = {}

    def get(self, key: int) -> int:
        # we search in the hashmap for the node
        # if there does not exist a node
        # the hashmap we are using is the key
        # and the value associated with the key is the node of
        # the doubly linked list
        node = self.hashtable.get(key, -1)

        # no node of such value found
        if not isinstance(node, Node):
            return -1

            # have to check if it is the same as the tail
        # if it is already at the tail we dont have to do anything
        self.linkedlist.place_end(node)
        # then we have to update the head

        # edge cases are where the node you are trying to get is the head or tail

        # have to check if there is only one node in the hashmap
        # move the node to the end of the doubly linked list

        return node.val

    def put(self, key: int, value: int) -> None:
        # we are either updating or adding a new key value pair into the hashmap
        # the edge cases are when we fill up the cache capacity
        if self.linkedlist.head is None or self.linkedlist.tail is None:
            # this basically means the cache is currently empty
            self.hashtable[key] = Node(key=key, val=value)
            self.linkedlist.head = self.hashtable[key]
            self.linkedlist.tail = self.hashtable[key]
            self.capacity = max(0, self.capacity - 1)
        else:
            if key in self.hashtable:
                node = self.hashtable[key]
                node.val = value

            else:
                node = Node(key=key, val=value)
                self.hashtable[key] = node
                old_head = self.linkedlist.head
                if self.capacity == 0:
                    if self.linkedlist.head == self.linkedlist.tail:
                        self.linkedlist.tail = node
                    else:
                        self.linkedlist.head = self.linkedlist.head.nxt
                    # that means we have to update the LRU cache
                    #
                    print(old_head.key)
                    self.hashtable.pop(old_head.key)
                else:
                    # we dont have to as we still have cache space in the cache

                    self.capacity = max(0, self.capacity - 1)
            # the key will still be at the end of the linked list regardless of whether
            # it was in it previously or not
            self.linkedlist.place_end(node)


class Node:
    def __init__(self, key, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class DoublyLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def place_end(self, node):
        if node != self.tail:
            previous = node.previous
            nxt = node.nxt
            node.nxt.previous = previous
            node.nxt = None
            self.tail.nxt = node
            self.tail = node

            if node == self.head:
                self.head = nxt

