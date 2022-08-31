class Trans_agency:
    def __init__(self, price):
        self.price = price

    def info(self):
        print("price:", self.price)


class Transport(Trans_agency):
    def __init__(self, speed, price):
        super().__init__(price)
        self.speed = speed

    def Time(self, distance):
        self.time = distance / self.speed

    def info(self):
        print("speed:", self.time)


class Car_transport(Transport):
    def __init__(self, speed, price):
        super().__init__(speed, price)

    def View_transport(self, view):
        self.view = view

    def info(self):
        print(f"Car transport time on the way: {self.time} hour")


class Railway_transport(Transport):
    def __init__(self, speed, price):
        super().__init__(speed, price)

    def View_transport(self, view):
        self.view = view

    def info(self):
        print(f"Railway_transport time: {self.time} hour")


class Air_transport(Transport):
    def __init__(self, speed, price):
        super().__init__(speed, price)

    def View_transport(self, view):
        self.view = view

    def info(self):
        print(f"Air_transport time: {self.time} hour")


class Cargo(Trans_agency):
    def __init__(self, weight, price):
        super().__init__(price)
        self.weight = weight * price

    def info(self):
        print(f"Cost delivery for weight cargo : {self.weight} rub")


class Direction(Trans_agency):
    def __init__(self, direction, distance, price):
        super().__init__(price)
        self.direction = direction
        self.distance = distance

    def info(self):
        print(f"Distance direction: {self.direction} {self.distance} km")


view1 = input("enter view transport (car, railway, air) : ")
if view1 == "car":
    direction1 = input("enter distance to the city (Brest, Grodno, Mogilev): ")
    if direction1 == "Brest":
        cargo1 = int(input("enter weight cargo: "))
        transport1 = Car_transport(90, 12)
        transport1.Time(200)
        cargo = Cargo(cargo1, 12)
        direction = Direction(direction1, 200, 12)
        transport1.info()
        direction.info()
        cargo.info()
    if direction1 == "Grodno":
        cargo1 = int(input("enter weight cargo: "))
        transport1 = Car_transport(90, 10)
        transport1.Time(230)
        cargo = Cargo(cargo1, 10)
        direction = Direction(direction1, 230, 10)
        transport1.info()
        direction.info()
        cargo.info()
    if direction1 == "Mogilev":
        cargo1 = int(input("enter weight cargo: "))
        transport1 = Car_transport(90, 8)
        transport1.Time(180)
        cargo = Cargo(cargo1, 8)
        direction = Direction(direction1, 180, 8)
        transport1.info()
        direction.info()
        cargo.info()
if view1 == "railway":
    direction1 = input("enter distance to the city (Brest, Grodno, Mogilev): ")
    if direction1 == "Brest":
        cargo1 = int(input("enter weight cargo: "))
        transport1 = Car_transport(70, 10)
        transport1.Time(200)
        cargo = Cargo(cargo1, 10)
        direction = Direction(direction1, 200, 10)
        transport1.info()
        direction.info()
        cargo.info()
    if direction1 == "Grodno":
        cargo1 = int(input("enter weight cargo: "))
        transport1 = Car_transport(70, 8)
        transport1.Time(230)
        cargo = Cargo(cargo1, 8)
        direction = Direction(direction1, 230, 8)
        transport1.info()
        direction.info()
        cargo.info()
    if direction1 == "Mogilev":
        cargo1 = int(input("enter weight cargo: "))
        transport1 = Car_transport(70, 6)
        transport1.Time(180)
        cargo = Cargo(cargo1, 6)
        direction = Direction(direction1, 180, 6)
        transport1.info()
        direction.info()
        cargo.info()
if view1 == "air":
    direction1 = input("enter distance to the city (Brest, Grodno, Mogilev): ")
    if direction1 == "Brest":
        cargo1 = int(input("enter weight cargo: "))
        transport1 = Car_transport(200, 20)
        transport1.Time(200)
        cargo = Cargo(cargo1, 20)
        direction = Direction(direction1, 200, 20)
        transport1.info()
        direction.info()
        cargo.info()
    if direction1 == "Grodno":
        cargo1 = int(input("enter weight cargo: "))
        transport1 = Car_transport(200, 18)
        transport1.Time(230)
        cargo = Cargo(cargo1, 18)
        direction = Direction(direction1, 230, 18)
        transport1.info()
        direction.info()
        cargo.info()
    if direction1 == "Mogilev":
        cargo1 = int(input("enter weight cargo: "))
        transport1 = Car_transport(200, 16)
        transport1.Time(180)
        cargo = Cargo(cargo1, 16)
        direction = Direction(direction1, 180, 16)
        transport1.info()
        direction.info()
        cargo.info()

