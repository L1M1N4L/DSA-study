class MyHashSet:

    def __init__(self):
        self.array = [0]*1000000

    def add(self, key: int) -> None:
        self.array[key] = 1
        return None

    def remove(self, key: int) -> None:
        self.array[key] = 0
        return None
    def contains(self, key: int) -> bool:
        if self.array[key] == 1:
            return True
        else:
            return False
        
        

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)