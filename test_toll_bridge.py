import pytest
from python import Vehicle, Motorbike, Car, Lorry, Bridge  # Replace 'your_module' with the name of your Python file

def test_motorbike_fee():
    bike = Motorbike("M1", 200)
    assert bike.calculate_fee() == 3.00

def test_car_fee_no_excess_weight():
    car = Car("C1", 1590)
    assert car.calculate_fee() == 5.00

def test_car_fee_with_excess_weight():
    car = Car("C1", 1700)  # 110 kg excess
    assert car.calculate_fee() == 5.00 + 0.10

def test_lorry_fee_under_limit():
    lorry = Lorry("L1", 7000)
    assert lorry.calculate_fee() == 10.00

def test_lorry_fee_over_limit():
    lorry = Lorry("L2", 8500)
    assert lorry.calculate_fee() == 15.00

def test_bridge_add_vehicle_within_limits():
    bridge = Bridge()
    bike = Motorbike("M1", 200)
    assert bridge.add_vehicle(bike) is True
    assert len(bridge.vehicles) == 1

def test_bridge_add_vehicle_exceeds_weight_limit():
    bridge = Bridge()
    lorry = Lorry("L1", 25000)  # 25000 kg
    bridge.add_vehicle(lorry)  # Should succeed
    assert bridge.calc_total_weight() == 25000

    lorry2 = Lorry("L2", 10000)  # This should exceed the total limit
    assert bridge.add_vehicle(lorry2) is False
    assert len(bridge.vehicles) == 1  # Still only one vehicle

def test_bridge_remove_vehicle():
    bridge = Bridge()
    bike = Motorbike("M1", 200)
    bridge.add_vehicle(bike)
    bridge.remove_vehicle("M1")
    assert len(bridge.vehicles) == 0

def test_bridge_remove_nonexistent_vehicle():
    bridge = Bridge()
    bridge.remove_vehicle("M1")  # Should not raise an error
    assert len(bridge.vehicles) == 0  # Still empty
