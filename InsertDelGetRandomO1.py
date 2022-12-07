# Implement the RandomizedSet class:

#     RandomizedSet() Initializes the RandomizedSet object.
#     bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
#     bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
#     int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

# You must implement the functions of the class such that each function works in average O(1) time complexity.
import random

class RandomizedSet:

    def __init__(self):
        # maintain both a list and a set
        # set is for insert/remove O(1) time
        # list is for random O(1) time
        self.list = []
        self.map = {}

    def insert(self, val: int) -> bool:
        # check if the value is in our map first
        if val in self.map:
            return False
        # add to our list and map, key is the val index is value
        # inserted into the list at the end, so our index is just len(list) - 1
        self.list.append(val)
        self.map[val] = len(self.list) - 1

        return True

    def remove(self, val: int) -> bool:
        # check if the value is not in the map
        if val not in self.map:
            return False
        # grab the list index of the value
        # do a swap with value and the last value
        # no need to swap last with the remove value, it gets popped anyways
        # make sure to update map with new index
        index = self.map[val]
        temp = self.list[-1]
        self.list[index] = temp
        self.list.pop()
        self.map[temp] = index
        del self.map[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(2))
print(obj.insert(3))
print(obj.remove(2))