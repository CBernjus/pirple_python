# Homework Assignment # 9 - Classes

import random


class Vehicle:

    def __init__(self, make, model, year, weight, needsMaintenance=False, tripsSinceMaintenance=0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

    def getMake(self):
        return self.make

    def setMake(self, make):
        self.make = make

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year

    def getWeight(self):
        return self.model

    def setWeight(self, weight):
        self.weight = weight

    def getNeedsMaintenance(self):
        return self.needsMaintenance

    def setNeedsMaintenance(self, needsMaintenance):
        self.needsMaintenance = needsMaintenance

    def getTripsSinceMaintenance(self):
        return self.tripsSinceMaintenance

    def setTripsSinceMaintenance(self, tripsSinceMaintenance):
        self.tripsSinceMaintenance = tripsSinceMaintenance
        if tripsSinceMaintenance > 100:
            self.setNeedsMaintenance(True)

    def Repair(self):
        self.setNeedsMaintenance(False)
        self.setTripsSinceMaintenance(0)

    def __str__(self):
        return f"{{{self.getMake()}, {self.getModel()}, {self.getYear()}, {self.getWeight()}, {self.getNeedsMaintenance()}, {self.getTripsSinceMaintenance()}}}"


class Car(Vehicle):

    def __init__(self,  make, model, year, weight, needsMaintenance=False, tripsSinceMaintenance=0, isDriving=False):
        super(Car, self).__init__(make, model, year, weight,
                                  needsMaintenance, tripsSinceMaintenance)
        self.isDriving = isDriving

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        self.isDriving = False
        self.setTripsSinceMaintenance(self.getTripsSinceMaintenance() + 1)

    def __str__(self):
        return super(Car, self).__str__ + (" is Driving" if self.isDriving else " is not Driving")


cars = []

car1 = Car("VW", "Polo", 2018, 3000)
car2 = Car("Audi", "TT", 2020, 2000)
car3 = Car("VW", "Passat", 2020, 4000)

cars.append(car1)
cars.append(car2)
cars.append(car3)

for car in cars:
    for _ in range(random.randint(0, 10)):
        car.Drive()
        car.Stop()
    print(str(car))


class Plane(Vehicle):

    def __init__(self,  make, model, year, weight, needsMaintenance=False, tripsSinceMaintenance=0, isFlying=False):
        super(Plane, self).__init__(make, model, year, weight,
                                    needsMaintenance, tripsSinceMaintenance)
        self.isFlying = isFlying

    def Fly(self):
        if self.getNeedsMaintenance:
            print("The Plane can't fly until it's repaired")
            return False
        self.isFlying = True

    def Land(self):
        self.isFlying = False
        self.setTripsSinceMaintenance(self.getTripsSinceMaintenance() + 1)

    def __str__(self):
        return super(Plane, self).__str__() + (" is Flying" if self.isFlying else " is not Flying")
