'''
4 classes: VehicleType, Vehicle, ParkingSpot, ParkingLot
VehicleType: An enum to represent different types of vehicles (e.g., motorcycle, car, truck).

Vehicle: A class to represent a vehicle, which has a type (VehicleType).

ParkingSpot: A class to represent a parking spot, which can be occupied by a vehicle or be empty. 
It should have methods to check if it's occupied and to park or remove a vehicle.


ParkingLot: A class to represent the parking lot, which contains multiple parking spots.
three types of parking spots: motorcycle spots, car spots, and truck spots.

'''


class VehicleType(Enum):
    MOTORCYCLE = "motorcycle"
    CAR = "car"
    TRUCK = "truck"

class Vehicle:
    def __init__(self, vehicle_type: VehicleType, license_plate: str):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: VehicleType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.parked_vehicle = None
        
    def is_occupied(self):
        return self.parked_vehicle is not None
    
    def can_fit(self,vehicle:Vehicle) -> bool:
        if self.spot_type == VehicleType.MOTORCYCLE:
            return vehicle.vehicle_type == VehicleType.MOTORCYCLE
        elif self.spot_type == VehicleType.CAR:
            return vehicle.vehicle_type in [VehicleType.MOTORCYCLE, VehicleType.CAR]
        elif self.spot_type == VehicleType.TRUCK:
            return vehicle.vehicle_type in [VehicleType.MOTORCYCLE, VehicleType.CAR, VehicleType.TRUCK]
        return False
    
    def park(self,vehicle:Vehicle) -> bool:
        if self.can_fit(vehicle) and not self.is_occupied():
            self.parked_vehicle = vehicle
            return True
        return False
    
    def unpark(self):
        self.parked_vehicle = None

class ParkingLot:
    def __init__(self, num_motorcycle_spots: int, num_car_spots: int, num_truck_spots: int):
        self.spots = []
    
    def add_spot(self,spot: ParkingSpot):
        self.spots.append(spot)

    def find_spot_for_vehicle(self, vehicle: Vehicle) -> ParkingSpot:
        for spot in self.spots:
            if spot.can_fit(vehicle) and not spot.is_occupied():
                return spot
        return None
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        spot = self.find_spot_for_vehicle(vehicle)
        if spot:
            return spot.park(vehicle)
        return False
    
    def unpark_vehicle(self, license_plate: str) -> bool:
        for spot in self.spots:
            if spot.is_occupied() and spot.parked_vehicle.license_plate == license_plate:
                spot.unpark()
                return True
        return False

    def available_spots(self):
        return [spot for spot in self.spots if not spot.is_occupied()]
    