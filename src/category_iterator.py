from src.category import Category

class CategoryIterator:
    def __init__(self, category: Category):
        self._products = category.products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._products):
            raise StopIteration
        result = self._products[self._index]
        self._index += 1
        return result