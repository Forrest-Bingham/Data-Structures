from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {}
        self.size = 0
        self.ordering = DoublyLinkedList()

        #[1]-[2]-[3]-[4]-[5]    [d]-[z]-[c]-[a]

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #Push it to the tail since it is most recently used
        print(key)
        #Check to see if key exists:
        if key in self.storage:
            #Move key to to end so it is most recent
            print("Checking to see if key is in storage...")
            node = self.storage[key]
            print(node.value, "---Node")
            self.ordering.move_to_end(node)
            #value[0] is the key, value[1] is the value
            return node.value[1]
        #If no key exists
        else:
            return None
        """
        Adds the given key-value pair to the cache. The newly-
        added pair should be considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache needs to be removed to make room. Additionally, in the
        case that the key already exists in the cache, we simply
        want to overwrite the old value associated with the key with
        the newly-specified value.
        """
    def set(self, key, value):
        
        #Adding an item puts it in the back since it is the most used
        #if key value pair exists, replace it with this current value
        if key in self.storage:
            node = self.storage[key]
            #Overwrite old value
            node.value = (key, value)
            #move this node to the tail
            self.ordering.move_to_end(node)
            return
        
        #If stack is at max capacity, erase least used and replace it with new item
        if self.size == self.limit:
            #get rid of least recently used element
            oldest_key = self.ordering.head.value[0]
            del self.storage[oldest_key]
            #Remove head node from the DLL
            self.ordering.remove_from_head()
            self.size -= 1

        #KEy is not in storage and still have room in our cache
        #Add the key and value
        self.ordering.add_to_tail((key, value))
        self.storage[key] = self.ordering.tail
        self.size += 1

#  def test_cache_overwrite_appropriately(self):
#         self.cache.set('item1', 'a')
#         self.cache.set('item2', 'b')
#         self.cache.set('item3', 'c')

#         self.cache.set('item2', 'z')

#         self.assertEqual(self.cache.get('item1'), 'a')
#         self.assertEqual(self.cache.get('item2'), 'z')