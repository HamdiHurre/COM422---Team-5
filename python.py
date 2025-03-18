from Vehicles.vehicle import Vehicle
from Vehicles.vehicle_children import Car, Lorry, Motorbike
from bridge import Bridge

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
