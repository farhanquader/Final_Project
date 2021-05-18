import random

class Bird:
    def __init__(self, row, col, type_of):
        self.row = row
        self.col = col
        self.type_of = type_of
        self.picture_taken = False

    def picture(self):
        self.picture_taken = True

class Coordinates:
    def __init__(self, height, width, num_of_birds):
        """"The constructor for the hypothetical map being used in the program.
            This Coordinates object will be called upon when creating a map"""
        self.height = height
        self.width = width
        self.num_of_birds = num_of_birds
        if (height * width) < num_of_birds:
            self.num_of_birds = (height * width) // 2
        self.birds = []
        self.populate_birds()

    def has_bird_in_location(self, row, col):
        for bird in self.birds:
            if bird.row == row and bird.col == col:
                return True
        return False

    def populate_birds(self):
        """This function serves as a randomizer to place birds in certain locations of the map"""
        for i in range(self.num_of_birds):
            is_bird_added = False
            while is_bird_added == False:
                row = random.randint(0, self.height)
                col = random.randint(0, self.width)
                if self.has_bird_in_location(row, col) == False:
                    random_type = random.randint(0, 4)
                    if random_type == 0:
                        type_of = "robin"
                    elif random_type == 1:
                        type_of = "ostrich"
                    elif random_type == 2:
                        type_of = "falcon"
                    else:
                        type_of = "penguin"
                    bird = Bird(row, col, type_of)
                    self.birds.append(bird)
                    is_bird_added = True
            i += 1

    def snap_picture_at(self, row, col):
        for bird in self.birds:
            if bird.row == row and bird.col == col:
                bird.picture()
                return bird
        return None

class Person:
    def __init__(self, name, film):
        """This creates the designated user with said name and amount of film.
            The constructor also provides the user's number of birds' photos taken"""
        self.name = name
        self.birds_snapped = []
        self.film = film

    def has_film(self):
        if self.film > 0:
            return True
        return False

    def snap_picture(self, row, col, map):
        if self.film > 0:
            bird = map.snap_picture_at(row, col)
            if bird != None:
                self.birds_snapped.append(bird)
                print("You got a photo of the bird")
            else:
                print("There is no bird there.")
            self.film -= 1
        else:
            print("You are out of film.")

if __name__ == "__main__":
    """This main method gives a good test/outlook of how the program
        should run normally."""
    coordinates = Coordinates(6, 5, 100)
    person = Person("Farhan", 10)
    while person.has_film():
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        person.snap_picture(row, col, coordinates)

"""class Collection_Birds:
    def __init(self, new_bird, new_coordinate):
        return None"""
