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