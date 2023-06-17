class Backpack:

    def __init__(self):
        self._contents = []
        self._max_size = 5

    def get_contents(self):
        return self._contents

    def set_contents(self, new_contents):
        if isinstance(new_contents, list):
            self._contents = new_contents

        else:
            print("Please enter a valid list")

my_backpack = Backpack()

my_backpack.set_contents("Water bottle")
print(my_backpack.get_contents())

