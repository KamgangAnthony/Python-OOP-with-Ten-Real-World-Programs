class Dog:

    def __init__(self, name, color, sex):
        self.name = name
        self._color = color
        self._sex = sex


    def get_sex(self):
        return self._sex

    def set_sex(self, new_sex):
        if isinstance(new_sex, str) and new_sex.isalpha():
            self._sex = new_sex

        else:
            print("Please enter a valid sex.")


my_dog = Dog("Bernard", "Black", "Male")
print("My dog's sex is:", my_dog.get_sex())

my_dog.set_sex("Female")

print("My dog's new sex is:", my_dog.get_sex())