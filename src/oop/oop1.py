# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#base class
class Vehicle:
    pass

#child class of Vehicle
class FlightVehicle(Vehicle):
    pass

#child class of FlightVehicle
class Airplane(FlightVehicle):
    pass

#child class of FlightVehicle
class Starship(FlightVehicle):
    pass

#child class of Vehicle
class GroundVehicle(Vehicle):
    pass

#child class of GroundVehicle
class Car(GroundVehicle):
    pass

#child class of GroundVehicle
class Motorcycle(GroundVehicle):
    pass