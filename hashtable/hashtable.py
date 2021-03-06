class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = [HashTableEntry(None, None)] * capacity
        self.num_elements = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_elements / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        hash_val = 14695981039346656037  # FNV offset basis value
        fnv_prime = 1099511628211

        for byte in key.encode():
            byte &= 0xffffffffffffffff
            hash_val *= fnv_prime
            hash_val ^= byte

        return hash_val

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % len(self.capacity)
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # check for capacity
        if self.get_load_factor() > 0.7:
            # upsize
            self.resize(self.get_num_slots() * 2)

        # generate index for key
        index = self.hash_index(key)

        # check to see if a value already exists at that key
        if self.capacity[index].key is not None:
            # check for key at head of list
            if self.capacity[index].key == key:
                # override head of list
                self.capacity[index].value = value
                return self.capacity[index].value
            # check for key in rest of list
            cur = self.capacity[index].next

            while cur is not None:
                # if value found, overwrite
                if cur.key == key:
                    cur.value = value
                    return cur.value
                # walk through list
                cur = cur.next

        # else, add to head
        new_entry = HashTableEntry(key, value)
        new_entry.next = self.capacity[index]
        self.capacity[index] = new_entry
        self.num_elements += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        try:
            if self.capacity[index].key == key:
                # override head of list
                old_head = self.capacity[index]
                self.capacity[index] = self.capacity[index].next
                self.num_elements -= 1
                return old_head
            # check for key in rest of list
            prev = self.capacity[index]
            cur = self.capacity[index].next

            while cur is not None:
                # if value found, overwrite
                if cur.key == key:
                    prev.next = cur.next
                    return cur
                # walk through list
                prev = prev.next
                cur = cur.next

        except KeyError:
            print("Key not found")
        
        # check for low capacity & resize if needed
        if self.get_load_factor() < 0.2:
            # if not below min capacity, downsize
            if self.get_num_slots() > MIN_CAPACITY:
                self.resize(self.get_num_slots() // 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # generate index for key
        index = self.hash_index(key)

        # walk list to look for key
        cur = self.capacity[index]

        while cur is not None:
            # if value found, overwrite
            if cur.key == key:
                return cur.value
            # walk through list
            cur = cur.next

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # save old hash table values
        old_table = self.capacity

        # reinitialize new table
        self.capacity = [HashTableEntry(None, None)] * new_capacity

        # reassign old values to new
        for entry in old_table:
            # loop through items in list and map to new list
            while entry.key is not None:
                self.put(entry.key, entry.value)
                entry = entry.next


if __name__ == "__main__":
    ht = HashTable(8)

    print(ht.get_num_slots())
    for bin in ht.capacity:
        print(bin)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
