# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

#     LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#     int get(int key) Return the value of the key if the key exists, otherwise return -1.
#     void put(int key, int value) Update the value of the key if the key exists. 
#     Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.

# Constraints:

#     1 <= capacity <= 3000
#     0 <= key <= 104
#     0 <= value <= 105
#     At most 2 * 105 calls will be made to get and put.

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# use a hashmap of Nodes to keep track of the least recent and most recent used keys
# left will be the least recent, right is most recent
# double linked list will keep track of the order
# whenever you get a key, remove it from the hashmap and re-add it
# whenever you put a key, check if it exists and update value
# if new, check for capacity and remove the left most node if it is over capacity

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity if capacity > 0 else 1
        self.cache = {}

        # left is least recently used, right is most recently used
        # 0 is used as a placeholder for knowing which node to insert to
        # insert will be Node <- 0 (right)
        # any access/update will update the right node
        # left is only used for getting the least recent node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = next.prev = node
        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        # get the nodes in cache
        if key in self.cache:
            # remove it from the cache and re-add it so it moves to the right of the cache
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # need to update the value if the key is already in
        # remove it since it has been accessed and re-add it to the right
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # cache cannot exceed capacity, remove the least recently used key which should be the last key in the cache
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(1, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4