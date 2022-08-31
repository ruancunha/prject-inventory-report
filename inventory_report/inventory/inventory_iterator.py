from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current = 0

    def __next__(self):
        data = self.data[self.current]
        if not data:
            raise StopIteration()
        else:
            self.current += 1
        return data
