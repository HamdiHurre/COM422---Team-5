from Vehicles.vehicle import Vehicle

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