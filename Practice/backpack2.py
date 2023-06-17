class BackpackTwo:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_item):
        if isinstance(new_item, list):
            self._items = new_item

        else:
            print("Enter a valid list of items")

my_backpack = BackpackTwo()
print(my_backpack.items)
my_backpack.items = "Fanta"

print(my_backpack.items)