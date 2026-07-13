class MyHashMap:

    def __init__(self):
        self.array = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.array[key] = value
    def get(self, key: int) -> int:
        if self.array[key] == None:
            return -1
        return self.array[key]        
        

    def remove(self, key: int) -> None:
        self.array[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)