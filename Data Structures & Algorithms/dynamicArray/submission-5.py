class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        if i < self.current_length:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.current_length:
            self.arr[i] = n 

    def pushback(self, n: int) -> None:
        if self.capacity == self.current_length:
            self.resize()
        self.arr[self.current_length] = n
        self.current_length += 1
        


    def popback(self) -> int:
        if self.current_length > 0:
            self.current_length -= 1
            return self.arr[self.current_length]
        raise IndexError("Pop from empty array")


    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity
        
        for i in range(self.current_length):
            newArr[i] = self.arr[i]
        self.arr = newArr


    def getSize(self) -> int:
        return self.current_length
        
    
    def getCapacity(self) -> int:
        return self.capacity 
