class LinkNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.hash_map = [LinkNode(0, 0) for _ in range(1001)]

    def put(self, key: int, value: int) -> None:
        index = key % 1000
        list_node = self.hash_map[index]
        while list_node.next:
            list_node = list_node.next
            if list_node.key == key:
                list_node.value = value
        list_node.next = LinkNode(key, value)

    def get(self, key: int) -> int:
        index = key % 1000
        list_node = self.hash_map[index]
        while list_node.next:
            list_node = list_node.next
            if list_node.key == key:
                return list_node.value
        return -1

    def remove(self, key: int) -> None:
        index = key % 1000
        list_node = self.hash_map[index]
        while list_node.next:
            if list_node.next.next and list_node.next.key == key:
                list_node.next = list_node.next.next
            else:
                list_node.next = None
            

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)