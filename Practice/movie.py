class Movie:

    def __init__(self, name, rating):
        self.name = name
        self._rating = rating

    @property
    def rating(self):
        print("Accessing getter...")
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 1 <= new_rating <= 5:
            print("Accessing setter...")
            self._rating = new_rating

        else:
            print("Enter a valid rating motherfucker !!!!!")

new_movie = Movie("Jason statham and the wolves", 4.2)
print(new_movie.rating)

new_movie.rating = -5

print(new_movie.rating)