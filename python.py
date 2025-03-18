from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    def __init__(self, registration_number, weight):
        self.registration_number = registration_number
        self.weight = weight

    @abstractmethod
    def calculate_fee(self):
        pass


# Child Classes
class Motorbike(Vehicle):
    def calculate_fee(self):
        return 3.00  # Fixed fee for motorbikes


class Car(Vehicle):
    BASE_FEE = 5.00
    AVERAGE_WEIGHT = 1590

    def calculate_fee(self):
        excess_weight = max(0, self.weight - self.AVERAGE_WEIGHT)
        additional_fee = (excess_weight // 100) * 0.10
        return self.BASE_FEE + additional_fee


class Lorry(Vehicle):
    BASE_FEE = 10.00
    HEAVY_LORRY_WEIGHT_LIMIT = 8000
    HEAVY_LORRY_FEE = 15.00

    def calculate_fee(self):
        if self.weight > self.HEAVY_LORRY_WEIGHT_LIMIT:
            return self.HEAVY_LORRY_FEE
        return self.BASE_FEE


# Bridge Class
class Bridge:
    MAX_VEHICLES = 20
    MAX_WEIGHT = 30000

    def __init__(self):
        self.vehicles = []

    def calc_total_weight(self):
        return sum(vehicle.weight for vehicle in self.vehicles)

    def add_vehicle(self, vehicle):
        if len(self.vehicles) >= self.MAX_VEHICLES:
            print(f"Cannot add vehicle {vehicle.registration_number}: bridge is full.")
            return False
        
        total_weight = self.calc_total_weight() + vehicle.weight
        if total_weight > self.MAX_WEIGHT:
            print(f"Cannot add vehicle {vehicle.registration_number}: weight limit exceeded.")
            return False
        
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.registration_number} added to the bridge.")
        return True

    def remove_vehicle(self, registration_number):
        vehicle_to_remove = next((v for v in self.vehicles if v.registration_number == registration_number), None)
        if vehicle_to_remove:
            self.vehicles.remove(vehicle_to_remove)
            print(f"Vehicle {registration_number} removed from the bridge.")
        else:
            print(f"Vehicle {registration_number} not found on the bridge.")


# Example Usage
if __name__ == "__main__":
    bridge = Bridge()

    bike = Motorbike("M1", 200)
    car = Car("C1", 1700)
    lorry = Lorry("L1", 8500)

    bridge.add_vehicle(bike)   # Should succeed
    bridge.add_vehicle(car)    # Should succeed
    bridge.add_vehicle(lorry)   # Should succeed

    print(f"Total weight on bridge: {bridge.calc_total_weight()} kg")
    
    bridge.remove_vehicle("C1")  # Should succeed
    bridge.add_vehicle(Lorry("L2", 20000))  # Should fail (exceeds weight limit)
