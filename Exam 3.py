class Alive:
    def __init__(self, count):
        self.count = count

    def info(self):
        print("count:", self.count)


class Plants(Alive):
    def __init__(self, koef_repr, count):
        super().__init__(count)
        self.koef_repr = koef_repr


    def grown(self):
        self.count *= self.koef_repr

    def sun(self):
        self.count -= int(self.count * 0.5)

    def info(self):
        print("count plants:", self.count)

    def rabbits_food(self, count_rabbits):
        self.count -= count_rabbits * 10

    def add_plants(self, counts_plants):
        self.count += counts_plants


class Rabbits(Alive):
    def __init__(self, koef_repr, koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def hunting(self):
        self.count -= int(self.count / 2)

    def info(self):
        print("count rabbits:", self.count)

    def foxs_food(self, count_foxs):
        self.count -= count_foxs * 5

    def take_away(self, count_rabbits):
        self.count -= count_rabbits


class Foxs(Alive):
    def __init__(self, koef_repr, koef_death, count):
        super().__init__(count)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def reproduction(self):
        self.count *= self.koef_repr

    def death(self):
        self.count -= int(self.count * self.koef_death)

    def hunting(self):
        self.count -= int(self.count / 2)

    def info(self):
        print("count foxs:", self.count)

    def take_away(self, count_foxs):
        self.count -= count_foxs

class Human:
    def konrol(self):
        choise = int(input("enter 1 - add plants: 2 - take away rabbits: 3 - take away foxs: enter: "))
        if choise == 1:
            count = int(input("enter count plants: - "))
            plants.add_plants(count)
        elif choise == 2:
            count = int(input("enter count rabbits: - "))
            rabbits.take_away(count)
        elif choise == 3:
            count = int(input("enter count foxs: - "))
            foxs.take_away(count)




plants = Plants(10, 500)
rabbits = Rabbits(5, 0.3, 50)
foxs = Foxs(3, 0.3, 10)
human = Human()

year = 1
print("begin:")
plants.info()
rabbits.info()
foxs.info()


while year <= 10:
    if plants.count // 10 <= rabbits.count:
        print("warning!!!!!")
        print("plants is very low")
    if rabbits.count // 5 <= foxs.count:
        print("warning!!!!!")
        print("rabbits is very low")
        human.konrol()

        plants.info()
        rabbits.info()
        foxs.info()

    if plants.count <= 0 or rabbits.count <= 0 or foxs.count <= 0:
        print("Fatality on year:", year)
        print("All our alive is death")
        break

    if year == 3 or year == 6 or year == 9:
        foxs.hunting()
    if year == 4 or year == 8:
        rabbits.hunting()
    if year == 2 or year == 5 or year == 7:
        plants.sun()

    plants.grown()
    plants.rabbits_food(rabbits.count)

    rabbits.foxs_food(foxs.count)
    rabbits.death()
    rabbits.reproduction()

    foxs.death()
    foxs.reproduction()



    print("year: ", year)

    plants.info()
    rabbits.info()
    foxs.info()

    year += 1

