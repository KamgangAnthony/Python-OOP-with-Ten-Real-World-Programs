class BackpackThree:

    def __init__(self):
        self._items = []

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)

        else:
            print("Enter a valid item.")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1

        else:
            return 0

    def has_item(self, item):
        return item in self._items

